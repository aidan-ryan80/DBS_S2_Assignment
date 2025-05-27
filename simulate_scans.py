# import random
# import time
# from datetime import datetime
# import json

# # Scan flag for running the simulator
# Scan: bool = True

# # ski_resorts_list = [(1, "Alpine Meadows"), (2, "Snowbird"), (3, "Whistler Blackcomb"), (4, "Aspen Snowmass"), (5, "Zermatt"), (6, "Chamonix"), (7, "Cortina d'Ampezzo"), (8, "Niseko"), (9, "Banff Sunshine"), (10, "St. Anton")]

# # Ski Pass and Ski Resort Data
# ski_data = {
#     "Alpine Meadows": [
#         (1, 'Day Pass', 55.00, 1),
#         (1, '2 Day Pass', 105.00, 2),
#         (1, '3 Day Pass', 150.00, 3),
#         (1, '4 Day Pass', 190.00, 4),
#         (1, '5 Day Pass', 225.00, 5),
#         (1, '6 Day Pass', 255.00, 6),
#         (1, '7 Day Pass', 280.00, 7)
#     ],
#     "Snowbird": [
#         (2, 'Da7y Pass', 65.00, 8),
#         (2, '2 Day Pass', 125.00, 9),
#         (2, '3 Day Pass', 180.00, 10),
#         (2, '4 Day Pass', 230.00, 11),
#         (2, '5 Day Pass', 275.00, 12),
#         (2, '6 Day Pass', 315.00, 13),
#         (2, '7 Day Pass', 350.00, 14)
#     ],
#     "Whistler Blackcomb": [
#         (3, 'Day Pass', 80.00, 15),
#         (3, '2 Day Pass', 155.00, 16),
#         (3, '3 Day Pass', 225.00, 17),
#         (3, '4 Day Pass', 290.00, 18),
#         (3, '5 Day Pass', 350.00, 19),
#         (3, '6 Day Pass', 405.00, 20),
#         (3, '7 Day Pass', 455.00, 21)
#     ],
#     "Aspen Snowmass": [
#         (4, 'Day Pass', 70.00, 22),
#         (4, '2 Day Pass', 135.00, 23),
#         (4, '3 Day Pass', 195.00, 24),
#         (4, '4 Day Pass', 250.00, 25),
#         (4, '5 Day Pass', 300.00, 26),
#         (4, '6 Day Pass', 345.00, 27),
#         (4, '7 Day Pass', 385.00, 28)
#     ],
#     "Zermatt": [
#         (5, 'Day Pass', 78.00, 29),
#         (5, '2 Day Pass', 150.00, 30),
#         (5, '3 Day Pass', 215.00, 31),
#         (5, '4 Day Pass', 275.00, 32),
#         (5, '5 Day Pass', 330.00, 33),
#         (5, '6 Day Pass', 380.00, 34),
#         (5, '7 Day Pass', 425.00, 35)
#     ],
#     "Chamonix": [
#         (6, 'Day Pass', 75.00, 36),
#         (6, '2 Day Pass', 145.00, 37),
#         (6, '3 Day Pass', 210.00, 38),
#         (6, '4 Day Pass', 270.00, 39),
#         (6, '5 Day Pass', 325.00, 40),
#         (6, '6 Day Pass', 375.00, 41),
#         (6, '7 Day Pass', 420.00, 42)
#     ],
#     "Cortina d'Ampezzo": [
#         (7, 'Day Pass', 52.00, 43),
#         (7, '2 Day Pass', 100.00, 44),
#         (7, '3 Day Pass', 143.00, 45),
#         (7, '4 Day Pass', 182.00, 46),
#         (7, '5 Day Pass', 217.00, 47),
#         (7, '6 Day Pass', 248.00, 48),
#         (7, '7 Day Pass', 275.00, 49)
#     ],
#     "Niseko": [
#         (8, 'Day Pass', 45.00, 50),
#         (8, '2 Day Pass', 85.00, 51),
#         (8, '3 Day Pass', 122.00, 52),
#         (8, '4 Day Pass', 156.00, 53),
#         (8, '5 Day Pass', 187.00, 54),
#         (8, '6 Day Pass', 215.00, 55),
#         (8, '7 Day Pass', 240.00, 56)
#     ],
#     "Banff Sunshine": [
#         (9, 'Day Pass', 68.00, 57),
#         (9, '2 Day Pass', 130.00, 58),
#         (9, '3 Day Pass', 190.00, 59),
#         (9, '4 Day Pass', 245.00, 60),
#         (9, '5 Day Pass', 295.00, 61),
#         (9, '6 Day Pass', 340.00, 62),
#         (9, '7 Day Pass', 380.00, 63)
#     ],
#     "St. Anton": [
#         (10, 'Day Pass', 76.00, 64),
#         (10, '2 Day Pass', 146.00, 65),
#         (10, '3 Day Pass', 210.00, 66),
#         (10, '4 Day Pass', 270.00, 67),
#         (10, '5 Day Pass', 325.00, 68),
#         (10, '6 Day Pass', 375.00, 69),
#         (10, '7 Day Pass', 420.00, 70)
#     ]
# }

# def generate_scan():
#     resort_name, resort_passes = random.choice(list(ski_data.items()))
#     resort_id, _, _, skipass_id = random.choice(resort_passes) # _, is used for ignoring values in the unpacked tuple

#     scan = {
#         "resort_name": resort_name,
#         "resort_id": resort_id,
#         "skipass_id": skipass_id,
#         "timestamp": datetime.now().isoformat()
#     }
#     return scan

# # Simulate continuous scan generation
# while Scan:
#     scan_data = generate_scan()
#     print(json.dumps(scan_data))  # Printing simulated scan
#     time.sleep(1)  # Waiting 1 second before simulating the next scan