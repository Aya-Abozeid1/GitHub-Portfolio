# Certificate and Secret Expiry Monitoring Logic App

## Overview

This repository contains a Logic App template designed to automate the monitoring of certificate and secret expirations for Azure Enterprise applications. The Logic App checks at regular intervals and sends warning notifications via Outlook to specified users when certificates or secrets are nearing expiration.

## Features

- **Automated Expiry Check**: The Logic App is set up to check at specified intervals for certificates and secrets approaching their expiration dates in Azure Enterprise applications.
- **Notification System**: When an expiration date is close, the Logic App sends a warning notification via Outlook to the configured users, giving them time to take action before expiry.
- **Customizable Intervals**: The frequency of the checks can be customized as needed to fit different operational requirements.
- **Azure Integration**: The app leverages Azure API to access and gather certificate and secret metadata.
- **Flexible Configuration**: Users and alert thresholds (such as how many days before expiration should trigger a notification) can be easily configured.

## Prerequisites

Before using this Logic App, ensure you have the following:

1. **Azure Subscription**: An active Azure account with permission to create Logic Apps and manage enterprise applications.
2. **Enterprise Applications**: The target applications within Azure Active Directory (AAD) that you want to monitor for expiring certificates and secrets.
3. **Outlook Email Setup**: A working Outlook email address to send notifications.

## Customization
You can customize the following:

- **Notification Schedule**: Adjust how often the Logic App runs by modifying the recurrence trigger in the workflow.
- **Expiration Threshold**: Modify the number of days before expiration that triggers a notification.
- **Recipient List**: Update the list of email recipients for the warning notifications in the app's configuration.

## Troubleshooting

- **No Notifications Sent**: Ensure that the Logic App is correctly connected to Azure Active Directory and that the appropriate permissions are granted.
- **Incorrect Expiry Data**: Verify that the enterprise applications being monitored have valid certificates and secrets configured.

## Contributing
- Contributions to improve the logic, error handling, or notification system are welcome. Feel free to open issues or submit pull requests.