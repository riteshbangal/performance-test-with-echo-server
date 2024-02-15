import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class EchoServerSimulation extends Simulation {

  val httpProtocol = http.baseUrl("http://localhost:8080") // Replace with your echo server's external IP

  val scn = scenario("Echo Server Simulation with 10 replicas")
    .exec(http("Echo Request")
      .get("/gatling_perf_test_app_local")
      .check(status.is(200))
    )

  setUp(
    // scn.inject(atOnceUsers(100000)) // Adjust the number of virtual users as needed
    scn.inject(rampUsersPerSec(1).to(1000).during(10.minutes))
  ).protocols(httpProtocol)
}
