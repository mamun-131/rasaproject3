## start gretting
* greet
  - utter_greet

## modem reboot path 1 - check modem
* modem_complain{"equipment": "modem"}
  - utter_modem_reboot_help_start
  - utter_modem_reboot_confirm_modem_has_power
  - utter_modem_reboot_modem_plugged_question
* affirm
  - utter_modem_reboot_can_be_solved_by_reboot
  - utter_modem_reboot_want_to_reboot_question
* affirm
  - utter_modem_reboot_connecting_to_your_modem
  - utter_modem_reboot_uptime_rebooting_options
* check_modem
  - action_Modem_Checking
  - utter_modem_reboot_please_confirm_again
  - utter_modem_reboot_want_to_reboot_question
* affirm
  - action_Modem_Reboot
  - utter_modem_reboot_uptime_checking_again_options
* affirm
  - action_Modem_Checking
  - utter_modem_reboot_resolve_your_issue_question
* affirm
  - utter_modem_reboot_anything_else_can_i_do_question
* affirm 
  - utter_modem_reboot_forwarding_to_router_bot
  - action_restart

## modem reboot path 1 - reboot modem
* modem_complain{"equipment": "modem"}
  - utter_modem_reboot_help_start
  - utter_modem_reboot_confirm_modem_has_power
  - utter_modem_reboot_modem_plugged_question
* affirm
  - utter_modem_reboot_can_be_solved_by_reboot
  - utter_modem_reboot_want_to_reboot_question
* affirm
  - utter_modem_reboot_connecting_to_your_modem
  - utter_modem_reboot_uptime_rebooting_options
* reboot_modem
  - action_Modem_Reboot
  - utter_modem_reboot_uptime_checking_again_options
* affirm
  - action_Modem_Checking
  - utter_modem_reboot_resolve_your_issue_question
* affirm
  - utter_modem_reboot_anything_else_can_i_do_question
* affirm 
  - utter_modem_reboot_forwarding_to_router_bot
  - action_restart

## modem reboot path 2
* modem_complain{"equipment": "modem"}
  - utter_modem_reboot_help_start
  - utter_modem_reboot_confirm_modem_has_power
  - utter_modem_reboot_modem_plugged_question
* deny
  - utter_modem_reboot_modem_light_on_question
* deny
  - utter_modem_reboot_modem_try_plugin_then_check_power_question
* deny
  - utter_modem_reboot_modem_try_check_power_outlet_question
* deny
  - utter_sorry
  - utter_connect_to_human_agent
* deny
  - utter_apologize
  - action_restart

## check modem
* check_modem
  - action_Modem_Checking
  - utter_modem_reboot_anything_else_can_i_do_question
* affirm 
  - utter_bot_top_line_options
* deny
  - utter_modem_reboot_forwarding_to_router_bot
  - action_restart

## reboot modem
* reboot_modem
  - action_Modem_Reboot
  - utter_modem_reboot_anything_else_can_i_do_question
* affirm 
  - utter_bot_top_line_options
* deny
  - utter_modem_reboot_forwarding_to_router_bot
  - action_restart

## story_goodbye
* goodbye
    - utter_goodbye

## bot challenge
*bot_challenge
  - action_default_fallback