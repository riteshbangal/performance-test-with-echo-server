import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class EchoServerSimulation extends Simulation {

  // val httpProtocol = http.baseUrl("http://echo-server-service") // Replace with your echo server's FQDN
  val httpProtocol = http.baseUrl("http://echo-server-service.poc.svc.cluster.local")

  val scn = scenario("Echo Server Simulation with 10 replicas")
    .exec(http("Echo Request")
      .get("/gatling_perf_test_app")
      .check(status.is(200))
    )

  setUp(
    scn.inject(atOnceUsers(100000)) // Adjust the number of virtual users as needed
    // scn.inject(rampUsersPerSec(1).to(10000).during(10.minutes)) // This example gradually increases the number of users from 1 to 10000 over a period of 10 minutes.
  ).protocols(httpProtocol)
}
