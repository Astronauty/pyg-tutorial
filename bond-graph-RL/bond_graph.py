import networkx as nx
from enum import Enum
from sympy import *

class BondGraphPortTypes(Enum):
    # Passive 1-port
    CAPACITANCE = 0
    INERTANCE = 1
    RESISTANCE = 2
    
    # Active 1-port
    EFFORT_SOURCE = 3
    FLOW_SOURCE = 4
    
    # Multiport/junctions
    ZERO_JUNCTION = 5
    ONE_JUNCTION = 6
    
    # Two-port
    TRANSFORMER = 7
    GYRATOR = 8

class GeneralizedVariables(Enum):
    # Power
    EFFORT = 0
    FLOW = 1
    
    # Energy
    MOMENTUM = 2
    DISPLACEMENT = 3
    
class BondGraphNode:
    def __init__(self, port_type:BondGraphPortTypes, max_ports:int, preferred_causality:GeneralizedVariables=None):
        self.port_type = port_type
        self.max_ports = max_ports
        
        self.e, self.f, self.p, self.q = symbols('e f p q')
            
        pass
    
    def integral_causality(self):
        match self.port_type:
            case BondGraphPortTypes.CAPACITANCE:
                return GeneralizedVariables.FLOW
            case BondGraphPortTypes.INERTANCE:
                return GeneralizedVariables.EFFORT
            case __:
                return None
    
    def get_effort_expr(self):
        pass
    
    def get_flow_expr(self):
        pass
            
            
class Capacitance(BondGraphNode):
    def __init__(self, capacitance):
        super().__init__(port_type=BondGraphPortTypes.CAPACITANCE, max_ports=1, preferred_causality=GeneralizedVariables.FLOW)
        self.C = capacitance
        pass
    
    def get_effort_expr(self):
        self.e = self.q/self.C
        return self.e
    

class Inertance(BondGraphNode):
    def __init__(self, inertance):
        super().__init__(port_type=BondGraphPortTypes.INERTANCE, max_ports=1)
        self.I = inertance
        pass
    
class Compliance(BondGraphNode):
    def __init__(self, compliance):
        super().__init__(port_type=BondGraphPortTypes.COMPLIANCE, max_ports=1)
        self.I = compliance
        pass
    

class EffortSource(BondGraphNode):
    def __init__(self):
        super().__init__(port_type=BondGraphPortTypes.EFFORT_SOURCE, max_ports=1)
        
        pass
class OneJunction(BondGraphNode):
    def __init__(self):
        super().__init__(port_type=BondGraphPortTypes.ONE_JUNCTION, max_ports=None)
        pass
class Transformer(BondGraphNode):
    def __init__(self, transformer_ratio):
        super().__init__(port_type=BondGraphPortTypes.TRANSFORMER, max_ports=2)
        self.tf_ratio = tf_ratio
        pass
class Gyrator(BondGraphNode):
    def __init__(self, gyrator_ratio):
        super().__init__(port_type=BondGraphPortTypes.GYRATOR, max_ports=2)
        self.gyrator_ratio = gyrator_ratio
        pass
class ZeroJunction(BondGraphNode):
    def __init__(self):
        super().__init__(port_type=BondGraphPortTypes.ZERO_JUNCTION, max_ports=None)
        pass
    



class BondGraphEdge:
    def __init__(self, causality):
        self.causality = causality # Causality that the source node of the directed edge imposes on the target node ()
        
        pass


class BondGraph():
    def __init__(self, num_effort_sources:int=0, num_flow_sources:int=0):
        """
        Creates a BondGraph system with a specified number of flow and effort sources to start.

        Args:
            num_effort_sources (int): _description_
            num_flow_sources (int): _description_
        """
        self.num_effort_sources = num_effort_sources
        self.num_flow_sources = num_flow_sources
        self.i = 0 # index for incrementally labeling nodes
        
        self.graph = nx.DiGraph()
    
    # Restrictive addition of ports (only allows valid bond graph ports)
    def add_port(self, port_type:BondGraphPortTypes, params:dict=None):
        """
        Adds a port to the bond graph. The port is labeled according to its type and the index of the port.

        Args:
            port (BondGraphNode): Specify the type of port to add to the bond graph. Each of the standard bond graph ports inherits the BondGraphNode class.
        """
        port_label = ""
        match port_type:
            case BondGraphPortTypes.CAPACITANCE:
                port_label = f"C_{self.i}"
            case BondGraphPortTypes.INERTANCE:
                port_label = f"I_{self.i}"
            case BondGraphPortTypes.RESISTANCE:
                port_label = f"R_{self.i}"
            case BondGraphPortTypes.EFFORT_SOURCE:
                port_label = f"Se_{self.i}"
            case BondGraphPortTypes.FLOW_SOURCE:
                port_label = f"Sf_{self.i}"
            case BondGraphPortTypes.ZERO_JUNCTION:
                port_label = f"0_{self.i}"
            case BondGraphPortTypes.ONE_JUNCTION:
                port_label = f"1_{self.i}"
                
        self.graph.add_node(self.i, port_type=port_type, param=params)
        self.i += 1
        return
    
    def add_bond(self, u, v, imposed_causality:GeneralizedVariables):
        """
        Creates a bond graph bond between nodes u and v. The directed edge corresponds to energy sign (i.e. power flows from the source node to the target node).
        Args:
            u (_type_): 
            v (_type_): _description_
            imposed_causality (GeneralizedVariables): _description_
        """
        self.graph.add_edge(u,v, imposed_causality=imposed_causality)
        
        # Check if the node is valid or not
        return
    
    def get_possible_bonds():
        return
