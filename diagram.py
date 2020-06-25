# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.integration import SQS

with Diagram("PubSub", show=False):
    EC2("Web-Server") >> SQS("Event") >> RDS("database")