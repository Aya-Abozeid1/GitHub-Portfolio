# Use the official PHP 7.2 image as the base
FROM php:7.2-fpm

# Set the shell to bash for easier command execution
SHELL ["/bin/bash", "-c"]

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget libssl-dev procps git locales gettext lsb-release vim \
    libpcre3 libpcre3-dev zlib1g zlib1g-dev build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PHP extension dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    libxml2 libxml2-dev libfreetype6 libfreetype6-dev libjpeg62-turbo \
    libjpeg62-turbo-dev libpng16-16 libpng-dev libbz2-dev libcurl4-openssl-dev \
    libexpat1-dev libmcrypt-dev libssl-dev libicu-dev libedit-dev libonig-dev \
    libxslt-dev libsqlite3-dev libdb-dev libedit-dev unixodbc unixodbc-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure and install PHP extensions
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) gettext soap gd zip pdo pdo_mysql mysqli intl xmlrpc \
    bcmath bz2 curl exif fileinfo ftp mbstring opcache sockets dba shmop sysvshm && \
    pecl install mcrypt sqlsrv-5.6.1 pdo_sqlsrv-5.6.1 && docker-php-ext-enable mcrypt sqlsrv pdo_sqlsrv

# Install and configure Nginx
RUN apt-get update && apt-get install --no-install-recommends -y nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Cleanup unnecessary packages to reduce image size
RUN apt-get remove --purge --auto-remove -y \
    libxml2-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev unixodbc-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/pear

# Copy your custom nginx.conf to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Install Composer and copy application files
COPY --from=composer:1.10 /usr/bin/composer /usr/bin/composer

# Set the working directory
WORKDIR /var/www

# Copy the application files and the .env file
COPY . .
# COPY .env.example .env

# Generate locales
RUN locale-gen

# Set ownership to the www-data user (default user for PHP-FPM) for the application files
RUN chown -R www-data:www-data /var/www

# Install PHP dependencies with Composer and optimize autoloading
RUN composer install --no-interaction --prefer-dist --optimize-autoloader -vvv || \
    { echo "Composer install failed"; exit 1; }

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and PHP-FPM services
CMD ["sh", "-c", "nginx -g 'daemon off;' & php-fpm && php artisan view:clear && php artisan cache:clear"]
