#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"
#include "nangraph.cc/graph.h"

TEST_CASE( "It can create a graph", "[creation]" ) {
  Graph g;

  g.addNode(1);
  g.addLink(1, 2);

  REQUIRE( g.getLinksCount() == 1 );
  REQUIRE( g.getNodesCount() == 2 );
  REQUIRE( g.getNode(1) != nullptr );
  REQUIRE( g.getNode(42) == nullptr );
}

TEST_CASE( "It can count degree", "[creation]" ) {
  Graph g;

  g.addLink(1, 2);

  auto first = g.getNode(1);

  REQUIRE( first->degree() == 1);
  REQUIRE( first->outDegree() == 1 );
  REQUIRE( first->inDegree() == 0 );

  auto second = g.getNode(2);
  REQUIRE( second->inDegree() == 1);
  REQUIRE( second->outDegree() == 0);
  REQUIRE( second->degree() == 1);
}
