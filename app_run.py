from bottle import route, run, request, abort, static_file

from fsm import TocMachine
import os

VERIFY_TOKEN = "123456789"
machine = TocMachine(
    states=[
        'user_state',
        'weather_state',
        'weather_city_state',
        'dcard_state',
        'pet_state',
        'pet_limit_state',
        'pet_unlimit_state',
        'sex_state',
        'sex_limit_state',
        'sex_unlimit_state',
        'google_state',
        'google_search_state'
    ],
    transitions=[
        {
            'trigger': 'user_advance',
            'source': 'user_state',
            'dest': 'weather_state',
            'conditions': 'is_going_to_weather_state'
        },
        {
            'trigger': 'user_advance',
            'source': 'user_state',
            'dest': 'dcard_state',
            'conditions': 'is_going_to_dcard_state'
        },
        {
            'trigger': 'user_advance',
            'source': 'user_state',
            'dest': 'google_state',
            'conditions': 'is_going_to_google_state'
        },
        {
            'trigger': 'weather_advance',
            'source': 'weather_state',
            'dest': 'weather_city_state',
        },
        {
            'trigger': 'dcard_advance',
            'source': 'dcard_state',
            'dest': 'pet_state',
            'conditions': 'is_goint_to_pet_state'
        },
        {
            'trigger': 'dcard_advance',
            'source': 'dcard_state',
            'dest': 'sex_state',
            'conditions': 'is_goint_to_sex_state'
        },
        {
            'trigger': 'pet_advance',
            'source': 'pet_state',
            'dest': 'pet_limit_state',
            'conditions': 'is_goint_to_pet_limit_state'
        },
        {
            'trigger': 'pet_advance',
            'source': 'pet_state',
            'dest': 'pet_unlimit_state',
            'conditions': 'is_goint_to_pet_unlimit_state'
        },
        {
            'trigger': 'sex_advance',
            'source': 'sex_state',
            'dest': 'sex_limit_state',
            'conditions': 'is_goint_to_sex_limit_state'
        },
        {
            'trigger': 'sex_advance',
            'source': 'sex_state',
            'dest': 'sex_unlimit_state',
            'conditions': 'is_goint_to_sex_unlimit_state'
        },
        {
            'trigger': 'google_advance',
            'source': 'google_state',
            'dest': 'google_search_state',
        },
        {
            'trigger': 'go_back',
            'source': [
                'weather_city_state',
                'pet_limit_state',
                'pet_unlimit_state',
                'sex_limit_state',
                'sex_unlimit_state',
                'google_search_state'
            ],
            'dest': 'user_state'
        }
    ],
    initial='user_state',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    # return 'OK'
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    # print('REQUEST BODY: ')
    # print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state == 'user_state':
            machine.user_advance(event)
        elif machine.state == 'weather_state':
            machine.weather_advance(event)
        elif machine.state == 'dcard_state':
            machine.dcard_advance(event)
        elif machine.state == 'pet_state':
            machine.pet_advance(event)
        elif machine.state == 'sex_state':
            machine.sex_advance(event)
        else:
            machine.google_advance(event)
        return 'OK'

@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    run(host='0.0.0.0', port=port, debug=True)
    #run(host='0.0.0.0', port=port, debug=True, reloader=True)
