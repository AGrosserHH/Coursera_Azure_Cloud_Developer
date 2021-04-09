import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):    

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # TODO: Get connection to database
    

    conn = psycopg2.connect(dbname="", user="", password="", host="")                                                                                 
    print("Connection established")
    cursor = conn.cursor()
    try:
        # TODO: Get notification message and subject from database using the notification_id
        cursor.execute("select status, message from public.notification where id = "+str(notification_id))
        notification = cursor.fetchall()

        # TODO: Get attendees email and name
        cursor.execute("select last_name,email from public.attendee")
        mail = cursor.fetchall()

        # https://docs.microsoft.com/de-de/azure/postgresql/flexible-server/connect-python
        # https://sendgrid.com/docs/for-developers/sending-email/v3-python-code-example/

        # TODO: Loop through each attendee and send an email with a personalized subject        
        for m in mail: 
            #print(m[1])           
            message = Mail(
                from_email='info@techconf.com',
                to_emails=m[1],
                subject='Updated',
                html_content='Message')            
            
        completed_date = datetime.utcnow()
        #print(completed_date)
        notification_status = 'Notified {} people'.format(len(mail))         
        logging.info('Python ServiceBus queue trigger processed message: %s',len(mail))

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        cursor.execute("UPDATE public.notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(notification_status, completed_date, notification_id))        
        #print(completed_date)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        conn.rollback()
    finally:
        # TODO: Close connection        
        cursor.close()
        conn.close()
