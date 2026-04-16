# Watchlists Realtime Speed-Up and Service Tests

Implemented a massive service tests executor that led to complex optimization investigations and reducing response times from seconds to milliseconds against big ISO20022 watchlists validations.

* Starting Point: Realtime API without a proper testing service and ~2 seconds of response time.
* Ending Point: Massive and configurable Service Test executor that led to optimizations; invoking parallel workers that send requests at the configured cadence.
* Results: Optimizations for our Realtime API reaching ~100ms for response time.