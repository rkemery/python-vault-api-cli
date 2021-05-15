#!/usr/bin/env python3

import requests
import time
import sys
from simple_term_menu import TerminalMenu
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

vault_addr = ''
vault_headers = {'X-Vault-Token' : ''}

def main():
    main_menu_title = " Main Menu\n"
    main_menu_items = ["vault_sys_audit", "vault_sys_auth", "quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_green", "fg_black")
    main_menu_exit = False

    main_menu = TerminalMenu(
            menu_entries=main_menu_items,
            title=main_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=main_menu_style,
            cycle_cursor=True,
            clear_screen=True,
    )
    
    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            vault_sys_audit()
            time.sleep(5)
        elif main_sel == 1:
            vault_sys_auth()
            time.sleep(5)
        elif main_sel == 2:
            main_menu_exit = True

def vault_sys_audit():
  try:
    response = requests.get(vault_addr+'/v1/sys/audit', headers=vault_headers, verify=False)
    response.raise_for_status()
    print(response.json())
  except requests.exceptions.HTTPError as errh:
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)

def vault_sys_auth():
  try:
    response = requests.get(vault_addr+'/v1/sys/auth', headers=vault_headers, verify=False)
    response.raise_for_status()
    print(response.json())
  except requests.exceptions.HTTPError as errh:
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)

if __name__ == "__main__":
    main()
