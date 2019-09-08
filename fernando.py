if __name__ == '__main__':
    import systemd.daemon, initio, redis

    print('Startup')
    initio.init(Motors=True);
    r = redis.Redis(host='192.168.0.1', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('fernando')
    print('Startup complete')
    systemd.daemon.notify('READY=1')

    try:
        for message in p.listen():
            cmd = message["data"]
            if cmd == "f":
                initio.forward(100)
            elif cmd == "b":
                initio.reverse(100)
            elif cmd == "l":
                initio.spinLeft(100)
            elif cmd == "r":
                initio.spinRight(100)
            elif cmd == "s":
                initio.stop()
    except:
        p.close()
        initio.stop()
        initio.cleanup()
        print("Goodbye")