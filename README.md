# python-vault-api-cli
![Vault Image](https://d1q6f0aelx0por.cloudfront.net/product-logos/library-vault-logo.png)

## Summary
Vault http api wrapper in python. Currently in early work phase.

## Usage
CLI menu driven, which currently supports GET and POST methods.
* Input vault_addr variable.
* Input vault token under vault_token variable.
* Profit?

## Logging
Each request is logged into an output.log file with a timestamp in the current working directory. 

## GET
Work is being done on adding more GET endpoints.

## POST
POST has just been implemented with /v1/sys/capbilities - e.g., lookup a token's capabilities.

## Updates
Each call now generates the response body but also pulls the API endpoint summary from documentation (this is not logged).
