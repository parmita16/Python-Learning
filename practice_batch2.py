# =====================================================================
# MORE REAL-WORLD SCENARIO PROBLEMS (extra practice batch 2)
# =====================================================================

# ---------------------------------------------------------------------
# EASY 5: Electricity bill calculator (tiered pricing + validation)
# ---------------------------------------------------------------------
def electricity_bill(units):
    if units < 0:
        return "Invalid input: units cannot be negative"

    # tiered rate: first 100 units cheap, next 100 more, rest most expensive
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

print(electricity_bill(250))  # 500 + 700 + 500 = 1700


# ---------------------------------------------------------------------
# EASY 6: Temperature converter with validation (C <-> F)
# ---------------------------------------------------------------------
def convert_temperature(value, from_unit, to_unit):
    valid_units = ("C", "F")
    if from_unit not in valid_units or to_unit not in valid_units:
        return "Invalid unit: use 'C' or 'F'"

    if from_unit == to_unit:
        return value

    if from_unit == "C" and to_unit == "F":
        return (value * 9 / 5) + 32
    else:  # F to C
        return (value - 32) * 5 / 9

print(convert_temperature(100, "C", "F"))  # 212.0
print(convert_temperature(32, "F", "C"))   # 0.0


# =====================================================================
# MEDIUM SECTION (more practice)
# =====================================================================

# ---------------------------------------------------------------------
# MEDIUM 4: ATM withdrawal simulation (denominations + validation)
# Why: classic "simulation" question - models a real machine's rules
# ---------------------------------------------------------------------
def atm_withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    if amount % 100 != 0:
        return "Amount must be a multiple of 100"
    if amount > balance:
        return "Insufficient balance"

    # figure out how many of each note to dispense, biggest first
    denominations = [2000, 500, 100]
    remaining = amount
    notes_given = {}
    for note in denominations:
        count = remaining // note
        if count > 0:
            notes_given[note] = count
        remaining = remaining % note

    new_balance = balance - amount
    return notes_given, new_balance

print(atm_withdraw(5000, 2600))
# ({2000: 1, 500: 1, 100: 1}, 2400)


# ---------------------------------------------------------------------
# MEDIUM 5: Parking lot system (simulation with multiple vehicle types)
# Why: "basic simulations" - tracks state changing over time
# ---------------------------------------------------------------------
class ParkingLot:
    def __init__(self, car_slots, bike_slots):
        self.car_slots_total = car_slots
        self.bike_slots_total = bike_slots
        self.cars_parked = 0
        self.bikes_parked = 0
        self.tickets = {}  # ticket_id -> vehicle_type
        self.next_ticket_id = 1

    def park_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            if self.cars_parked >= self.car_slots_total:
                return "No car slots available"
            self.cars_parked += 1
        elif vehicle_type == "bike":
            if self.bikes_parked >= self.bike_slots_total:
                return "No bike slots available"
            self.bikes_parked += 1
        else:
            return "Unknown vehicle type"

        ticket_id = self.next_ticket_id
        self.tickets[ticket_id] = vehicle_type
        self.next_ticket_id += 1
        return "Parked. Ticket ID: " + str(ticket_id)

    def remove_vehicle(self, ticket_id):
        if ticket_id not in self.tickets:
            return "Invalid ticket ID"
        vehicle_type = self.tickets.pop(ticket_id)
        if vehicle_type == "car":
            self.cars_parked -= 1
        else:
            self.bikes_parked -= 1
        return "Vehicle with ticket " + str(ticket_id) + " has left"

    def available_slots(self):
        return {
            "car": self.car_slots_total - self.cars_parked,
            "bike": self.bike_slots_total - self.bikes_parked,
        }

lot = ParkingLot(car_slots=2, bike_slots=2)
print(lot.park_vehicle("car"))     # Parked. Ticket ID: 1
print(lot.park_vehicle("car"))     # Parked. Ticket ID: 2
print(lot.park_vehicle("car"))     # No car slots available
print(lot.available_slots())       # {'car': 0, 'bike': 2}
print(lot.remove_vehicle(1))       # Vehicle with ticket 1 has left
print(lot.available_slots())       # {'car': 1, 'bike': 2}


# ---------------------------------------------------------------------
# MEDIUM 6: Shopping cart with discount rules (multi-condition validation)
# Why: "data validation with multiple conditions" - several rules stack
# ---------------------------------------------------------------------
def calculate_cart_total(items, is_member=False, coupon_code=None):
    # items: list of (price, quantity) tuples
    subtotal = 0
    for price, quantity in items:
        if price < 0 or quantity < 0:
            return "Invalid item: price and quantity must be non-negative"
        subtotal += price * quantity

    discount = 0

    # membership discount
    if is_member:
        discount += subtotal * 0.10

    # coupon discount - only valid on orders over 1000, one use
    if coupon_code == "SAVE20":
        if subtotal >= 1000:
            discount += subtotal * 0.20
        # if under 1000, coupon silently doesn't apply (still valid input)

    # discounts can't exceed the subtotal itself
    if discount > subtotal:
        discount = subtotal

    total = subtotal - discount
    return round(subtotal, 2), round(discount, 2), round(total, 2)

cart = [(500, 2), (250, 1)]  # subtotal = 1250
print(calculate_cart_total(cart, is_member=True, coupon_code="SAVE20"))
# subtotal=1250.0, discount = 125 (member) + 250 (coupon) = 375.0, total=875.0


# ---------------------------------------------------------------------
# MEDIUM 7: Restaurant order queue simulation (FIFO with priority orders)
# Why: models real-world queue behavior over time - a true "simulation"
# ---------------------------------------------------------------------
class OrderQueue:
    def __init__(self):
        self.regular_queue = []
        self.priority_queue = []  # e.g. VIP or delivery-app rush orders

    def add_order(self, order_id, is_priority=False):
        if is_priority:
            self.priority_queue.append(order_id)
        else:
            self.regular_queue.append(order_id)
        return "Order " + str(order_id) + " added"

    def serve_next(self):
        # priority orders always served first
        if self.priority_queue:
            return self.priority_queue.pop(0)
        elif self.regular_queue:
            return self.regular_queue.pop(0)
        else:
            return "No orders in queue"

q = OrderQueue()
q.add_order(101)
q.add_order(102, is_priority=True)
q.add_order(103)
print(q.serve_next())  # 102 (priority jumps ahead)
print(q.serve_next())  # 101
print(q.serve_next())  # 103
