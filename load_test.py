import invokust

settings = invokust.create_settings(
    locustfile="locusttest.py",
    host="http://127.0.0.1:88",
    num_users=1000,
    spawn_rate=50,
    run_time="1m"
)

loadtest = invokust.LocustLoadTest(settings=settings)
loadtest.run()
loadtest.stats()