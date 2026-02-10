tickets= {}
def assign_tickets(ticket_id,title,user_email):
    if ticket_id not in tickets:
        tickets[ticket_id] = {'title':title,'user_email':user_email,'status':'open'}
        print('Ticket assigned')
    else:
        print('Ticket already assigned')
    return

def remove_tickets(ticket_id):
    if ticket_id in tickets:
        del[tickets[ticket_id]]
    else:
        print('ticket not found')
    return

def update_ticket_status(ticket_id,statusupdation):
    if ticket_id in tickets:
        tickets[ticket_id]['status']=statusupdation
        print('status changed')
    else:
        print('ticket not found')
    return

assign_tickets(101,'suvi','suvi@gmail')
print(tickets)

