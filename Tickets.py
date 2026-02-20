# Write a function called assign_ticket - ticket_id, title, user_email
# Takes a unique ticket_id, a title, and an user_email .
# 1. assign_ticket
# 2. update_ticket_status
# 3. Remove a Ticket

tickets= {}
def assign_tickets(ticket_id,title,user_email):
    if ticket_id not in tickets:
        tickets[ticket_id] = {'title':title,'user_email':user_email,'status':'open'}
        print('Ticket assigned')
    else:
        print('Ticket already assigned')

def remove_tickets(ticket_id):
    if ticket_id in tickets:
        del tickets[ticket_id]
    else:
        print('ticket not found')

def update_ticket_status(ticket_id,statusupdation):
    if ticket_id in tickets:
        tickets[ticket_id]['status']=statusupdation
        print('status changed')
    else:
        print('ticket not found')

assign_tickets(101,'suvi','suvi@gmail')
print(tickets)

