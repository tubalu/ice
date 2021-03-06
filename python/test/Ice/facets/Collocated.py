#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2018 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import Ice
from TestHelper import TestHelper
TestHelper.loadSlice("Test.ice")
import TestI
import AllTests


class Collocated(TestHelper):

    def run(self, args):

        with self.initialize(args=args) as communicator:
            communicator.getProperties().setProperty("TestAdapter.Endpoints", self.getTestEndpoint())
            adapter = communicator.createObjectAdapter("TestAdapter")
            adapter.add(TestI.DI(), Ice.stringToIdentity("d"))
            adapter.addFacet(TestI.DI(), Ice.stringToIdentity("d"), "facetABCD")
            adapter.addFacet(TestI.FI(), Ice.stringToIdentity("d"), "facetEF")
            adapter.addFacet(TestI.HI(communicator), Ice.stringToIdentity("d"), "facetGH")

            # adapter.activate() // Don't activate OA to ensure collocation is used.

            AllTests.allTests(self, communicator)
