#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"
#include "nangraph/graph.h"

TEST_CASE( "It can create a graph", "[creation]" ) {
  Graph g;

  g.addNode(1);
  g.addLink(1, 2);

  REQUIRE( g.getLinksCount() == 1 );
  REQUIRE( g.getNodesCount() == 2 );
  REQUIRE( g.getNode(1) != nullptr );
  REQUIRE( g.getNode(42) == nullptr );
}
