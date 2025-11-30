from smle import SMLE
from smle.notification.services import Discord, Telegram

app = SMLE()
app.register_notification_services([Discord, Telegram])

@app.entrypoint
def main(args):

    # 'args' contains your smle.yaml configurations
    message = f"Training with learning rate: {args['training']['lr']}"

    app.notify(message)
    print(message)

    # Your logic here...

if __name__ == "__main__":
    app.run()