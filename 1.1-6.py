'''
Problem: Traffic Signal Optimization

Batch Processing (All Input Available):
A city transportation department analyzes traffic flow data to reprogram signal timing citywide. They have complete datasets from traffic sensors covering months of historical patterns - rush hour volumes, weekend flows, seasonal variations, and special events. With this full dataset, they can run sophisticated optimization algorithms that consider all intersections simultaneously, finding globally optimal timing patterns that minimize citywide congestion. The analysis takes hours or days, but produces the best possible signal coordination.

Streaming Processing (Input Arrives Over Time):
The same intersections use adaptive traffic control systems that respond to real-time conditions. Sensors detect approaching vehicles, but the system must decide signal timing based only on current and recent observations - it cannot wait to see what traffic will look like in 30 minutes. When accident reports arrive or sudden weather changes traffic patterns, the system must immediately adjust timing with incomplete information. It uses approximation algorithms that make good decisions quickly rather than waiting for perfect information that may never come.

Key Difference:
The batch system optimizes for the best possible long-term solution using complete information, while the streaming system optimizes for acceptable real-time responses using partial information. Both solve the same fundamental problem - optimizing traffic flow - but the availability of input data completely changes the algorithmic approach and acceptable solution quality.
'''