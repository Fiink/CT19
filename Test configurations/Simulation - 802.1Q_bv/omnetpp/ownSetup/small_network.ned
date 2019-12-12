//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package ownSetup;

import inet.node.ethernet.Eth1G;

//
// Small sample network with three hosts and one switch that shows how to 
// configure the IEEE 802.1Q Model. Configuration in omnetpp.ini
// - 80ns Tick length
//
network small_network
{
    parameters:
        @display("bgb=291,134,white");
    submodules:
        node1: Node1 {
            @display("p=39,70");
        }

        node2: Node2 {
            @display("p=220.8,33.12");
        }

        switch1: Switch1 {
            parameters:
                @display("p=147,70");
            gates:
                ethg[3];
        }
        node3: Node3 {
            @display("p=220.8,107.64");
        }
    connections:
        //
        // The example uses a simple star topology
        //
        node1.ethg <--> Eth1G {  length = 0.5m; } <--> switch1.ethg[0];
        node2.ethg <--> Eth1G {  length = 0.5m; } <--> switch1.ethg[1];
        node3.ethg <--> Eth1G {  length = 0.5m; } <--> switch1.ethg[2];
}
