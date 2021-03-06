import systemd.daemon
import initio
import redis


def execute():
    print('Startup')

    initio.init(Motors=True)

    cmd_forwards = 'f'
    cmd_backwards = 'b'
    cmd_left = 'l'
    cmd_right = 'r'
    cmd_stop = 's'
    cmd_query = '?'

    r = redis.Redis(host='192.168.0.1', port=6379,
                    db=0, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('fernando')

    r.publish('services', 'fernando.on')
    systemd.daemon.notify('READY=1')
    print('Startup complete')

    try:
        initio.stop()
        r.publish('fernando.status', cmd_stop)

        last_cmd = cmd_stop

        for message in p.listen():
            cmd = message['data']

            if cmd == cmd_forwards:
                initio.forward(100)
            elif cmd == cmd_backwards:
                initio.reverse(100)
            elif cmd == cmd_left:
                initio.spinLeft(100)
            elif cmd == cmd_right:
                initio.spinRight(100)
            elif cmd == cmd_stop:
                initio.stop()
            elif cmd == cmd_query:
                # Don't need to do anything in this case
                pass

            if cmd != cmd_query:
                last_cmd = cmd

            r.publish('fernando.status', last_cmd)
    except:
        p.close()

        initio.stop()
        initio.cleanup()

        r.publish('services', 'fernando.off')
        print('Goodbye')


if __name__ == '__main__':
    execute()
