#!/usr/bin/env python2.7
from operator import truediv
from werkzeug.middleware.proxy_fix import ProxyFix
import uuid
import requests
from flask import Flask, flash, json, render_template, session, request, redirect, url_for
from flask_session import Session  # https://pythonhosted.org/Flask-Session
import msal
import app_config

import sys
import os

# Flask Import
from flask import Flask, request, redirect, render_template, url_for
from flask import jsonify, abort, make_response
import mysql.connector
#import MySQLdb  # type: ignore
from importlib import reload

# Toekn and URL check import
from check_encode import random_token, url_check
from display_list import list_data

from sql_table import mysql_table


# Import Loggers
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import traceback
import imp

# Setting UTF-8 encoding
print((sys.executable))
imp.reload(sys)
# #sys.setdefaultencoding('UTF-8')
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
# app.config.from_object('config')
app.config.from_object(app_config)
Session(app)

shorty_host = app_config.domain

# MySQL configurations

host = app_config.host
user = app_config.user
passwrd = app_config.passwrd
db = app_config.db

# This section is needed for url_for("foo", _external=True) to automatically
# generate http scheme when this sample is running on localhost,
# and to generate https scheme when it is deployed behind reversed proxy.
# See also https://flask.palletsprojects.com/en/1.0.x/deploying/wsgi-standalone/#proxy-setups
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)



@app.route("/", methods=["GET", "POST"])
def index():
    # user = session.get('user')
    # user_json = json.dumps(user)
    if not session.get("user"):
        # flash(user_json)
        return redirect(url_for("login"))
    else:
       return redirect(url_for("web"))

@app.route("/web", methods=["GET", "POST"])
def web():

    # user=request.args.get("user")
    # version=request.args.get("version")
    conn = mysql.connector.connect(host=host, user=user, password=passwrd, database=db) # type: ignore
    cursor = conn.cursor()

    # Return the full table to displat on index.
    list_sql = "SELECT * FROM WEB_URL;"
    cursor.execute(list_sql)
    result_all_fetch = cursor.fetchall()
    # return jsonify(result_all_fetch)
    if request.method == 'POST':
        og_url = request.form.get('url_input')
        custom_suff = request.form.get('url_custom')
        tag_url = request.form.get('url_tag')
        if custom_suff == '':
            token_string = random_token()
        else:
            token_string = custom_suff
        if og_url != '':
            # if url_check(og_url) == True:

            # Check's for existing suffix
            check_row = "SELECT S_URL FROM WEB_URL WHERE S_URL = %s FOR UPDATE"
            cursor.execute(check_row, (token_string,))
            check_fetch = cursor.fetchone()

            if (check_fetch is None):
                insert_row = """
						INSERT INTO WEB_URL(URL , S_URL , TAG) VALUES( %s, %s , %s)
						"""
                result_cur = cursor.execute(
                    insert_row, (og_url, token_string, tag_url,))
                conn.commit()
                conn.close()
                e = ''
                return render_template('index.html', shorty_url=shorty_host+token_string) # type: ignore
            else:
                e = "The Custom suffix already exists . Please use another suffix or leave it blank for random suffix."
                return render_template('index.html', table=result_all_fetch, host=shorty_host, error=e)
            # else:
            # 	print(og_url)
            # 	e = "URL entered doesn't seem valid , Enter a valid URL."
            # 	return render_template('index.html2' ,table = result_all_fetch, host = shorty_host,error = e)

        else:
            e = "Enter a URL."
            return render_template('index.html', table=result_all_fetch, host=shorty_host, error=e)
    else:
        e = ''
        return render_template('index.html', table=result_all_fetch, host=shorty_host, error=e)


@app.route("/login")
def login():
    # Technically we could use empty list [] as scopes to do just sign in,
    # here we choose to also collect end user consent upfront
    session["flow"] = _build_auth_code_flow(scopes=app_config.SCOPE)
    return render_template("login.html", auth_url=session["flow"]["auth_uri"], version=msal.__version__)


# Its absolute URL must match your app's redirect_uri set in AAD
@app.route(app_config.REDIRECT_PATH)
def authorized():
    try:
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args)
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    except ValueError:  # Usually caused by CSRF
        pass  # Simply ignore them
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()  # Wipe out user and its token cache from session
    return redirect(  # Also logout from your tenant's web session
        app_config.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))


@app.route("/graphcall")
def graphcall():
    token = _get_token_from_cache(app_config.SCOPE)
    if not token:
        return redirect(url_for("login"))
    graph_data = requests.get(  # Use token to call downstream service
        app_config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
    ).json()
    return render_template('display.html', result=graph_data)


def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache


def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()


def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
        client_credential=app_config.CLIENT_SECRET, token_cache=cache)


def _build_auth_code_flow(authority=None, scopes=None):
    return _build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=url_for("authorized", _external=True))


def _get_token_from_cache(scope=None):
    cache = _load_cache()  # This web app maintains one cache per session
    cca = _build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        _save_cache(cache)
        return result


app.jinja_env.globals.update(
    _build_auth_code_flow=_build_auth_code_flow)  # Used in template


@app.route('/analytics/<short_url>')
def analytics(short_url):

    info_fetch, counter_fetch, browser_fetch, platform_fetch = list_data(
        short_url)
    return render_template("data.html", host=shorty_host, info=info_fetch, counter=counter_fetch,
                           browser=browser_fetch, platform=platform_fetch)

# Rerouting funciton

@app.route('/<short_url>')
def reroute(short_url):

    conn = mysql.connector.connect(hhost=host, user=user, password=passwrd, database=db) # type: ignore
    cursor = conn.cursor()
    platform = request.user_agent.platform
    browser = request.user_agent.browser
    counter = 1

    # Platform , Browser vars

    browser_dict = {'firefox': 0, 'chrome': 0, 'safari': 0, 'other': 0}
    platform_dict = {'windows': 0, 'iphone': 0,
                     'android': 0, 'linux': 0, 'macos': 0, 'other': 0}

    # Analytics
    if browser in browser_dict:
        browser_dict[browser] += 1
    else:
        browser_dict['other'] += 1

    if platform in platform_dict:
        platform_dict[platform] += 1
    else:
        platform_dict['other'] += 1

    cursor.execute("SELECT URL FROM WEB_URL WHERE S_URL = %s;", (short_url,))

    try:
        new_url = cursor.fetchone()[0]
        print(new_url)
        # Update Counters

        counter_sql = "\
				UPDATE {tn} SET COUNTER = COUNTER + {og_counter} , CHROME = CHROME + {og_chrome} , FIREFOX = FIREFOX+{og_firefox} ,\
				SAFARI = SAFARI+{og_safari} , OTHER_BROWSER =OTHER_BROWSER+ {og_oth_brow} , ANDROID = ANDROID +{og_andr} , IOS = IOS +{og_ios},\
				WINDOWS = WINDOWS+{og_windows} , LINUX = LINUX+{og_linux}  , MAC =MAC+ {og_mac} , OTHER_PLATFORM =OTHER_PLATFORM+ {og_plat_other} WHERE S_URL = %s;".\
            format(tn="WEB_URL", og_counter=counter, og_chrome=browser_dict['chrome'], og_firefox=browser_dict['firefox'],
                   og_safari=browser_dict['safari'], og_oth_brow=browser_dict[
                       'other'], og_andr=platform_dict['android'], og_ios=platform_dict['iphone'],
                   og_windows=platform_dict['windows'], og_linux=platform_dict['linux'], og_mac=platform_dict['macos'], og_plat_other=platform_dict['other'])
        res_update = cursor.execute(counter_sql, (short_url, ))
        conn.commit()
        conn.close()

        return redirect(new_url)

    except Exception as e:
        e = "Something went wrong.Please try again."
        return render_template('404.html'), 404

# Search results


@app.route('/search',  methods=['GET', 'POST'])
def search():
    s_tag = request.form.get('search_url')
    if s_tag == "":
        return render_template('index.html', error="Please enter a search term")
    else:
        conn = mysql.connector.connect(host=host, user=user, password=passwrd, database=db) # type: ignore
        cursor = conn.cursor()

        search_tag_sql = "SELECT * FROM WEB_URL WHERE TAG = %s"
        cursor.execute(search_tag_sql, (s_tag, ))
        search_tag_fetch = cursor.fetchall()
        conn.close()
        return render_template('search.html', host=shorty_host, search_tag=s_tag, table=search_tag_fetch)


@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr,
                 request.method, request.scheme, request.full_path, response.status)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                 timestamp, request.remote_addr, request.method,
                 request.scheme, request.full_path, tb)
    return make_response(e, 405)


if __name__ == "__main__":

    handler = RotatingFileHandler('shorty.log', maxBytes=100000, backupCount=3)
    logger = logging.getLogger('tdm')
    # logger.setLevel(logging.ERROR)
    # new_func(handler, logger)
    # app.run(host='127.0.0.1' , port=5000)
    app.debug=True
    app.run(host='0.0.0.0' , port=5000)
