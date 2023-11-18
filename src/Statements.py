# -*- coding: utf-8 -*-

class Language():
    pass

#EN = Language()
IT = Language()

# --- IT Statements --- #
    # Text message
IT.Start = "Hey, Netflixers! 😎\nWho among you $$ shares the account with? 👇"
IT.UseThis = "⚠️ A setup procedure is already active, use this message. ☝️\n\nIf it was accidentally deleted, restart the setup by pressing here 👇"
IT.ConfirmList = "Do you confirm the list of participants?"
IT.Schedule = "📆 On what *day of the month* does your subscription renew?"
IT.ConfirmSchedule = "Do you confirm that your Netflix subscription renews on the *$$*?"
IT.Done = "Done! So...\n\n🎬 The Netflixers are:\n*$$*\n📆 The subscription renews on the *$$* of every month.\n🔔 Notifications are *active*.\n\nEnjoy watching! 😎"
IT.TimeToPay = "📢 Another month has passed, to continue watching all the TV series on Netflix you need to pay your part.\n\nIt's *$$€ each*. 💸"
IT.EveryonePaid = "Everyone has paid their share! Next appointment on *$$*.\n\n*Enjoy Netflix!* 😎"
IT.AlreadyConfigured = "Settings for this group have already been confirmed or a configuration procedure is in progress. If you need to start over, press below"
IT.NewConfig = "To reconfigure the group, press 👉 /start"
IT.ConfirmReset = "Are you sure you want to reset the settings? *This action is irreversible.*"
IT.PaymentAccepted = "The payment of $$ has been *accepted*! ✅"
    # Callback query
IT.MaxReached = "⚠️ The maximum number of participants (4) has already been reached!"
IT.AlreadySigned = "You're already a Netflixer! 😎\nIf you pressed by mistake or changed your mind, you can unsubscribe from the list by tapping on your name."
IT.AtLeastOneUser = "⚠️ At least one participant is required to proceed."
IT.NotAdmin = "You're not the administrator, sorry. 🙁"
IT.AlreadyPayed = '$$ has already paid! 💰'
IT.Resetted = 'The group settings have been successfully reset! ✅'
IT.NotPermitted = '️⚠️ Action not permitted.'
IT.Added = "Added ✅"
IT.Removed = "Removed ✅"
IT.IsWaiting = "⚠️ You are already waiting for confirmation."
IT.WaitingFor = "⏳ Waiting for the administrator to confirm the payment has been received."
IT.AlmostDone = "⏳ Almost there..."
    # Private Chat Statements
IT.Welcome = ("Hello *$$*! I am a bot, and I will help you manage your Netflix group. 😊\n\n"
             "Before starting you should know that I am still in an _alpha_ development stage, so unexpected behavior might occur. "
             "If you encounter any problems, or for anything else, please contact my programmer @LinkOut, he will be happy to help. "
             "If you are a programmer too, you can find me on [GitHub](https://github.com/xLinkOut/cagateisoldibot).\n\n"
             "Here's some useful information: to function, add me to a group using the nickname @cagateisoldibot. "
             "The first step will be to 📝 mark all the people who share Netflix with you, then a quick setup will follow where you can indicate the 📆 day of the month when the subscription renews. "
             "On that day, every month, I will send a notification with a list where people who have paid can sign up, and where you will then have to confirm the payment.\n\n"
             "*That's it!* New features are in development. This project is completely free, but servers cost; if you are interested in contributing you will find the 🎁 Donate button in the keyboard below.")
IT.Donate = "To support the project you can donate via PayPal on [this page](https://paypal.me/LCirillo). ❤️"
IT.About = "Made with ❤️ and a lot of `</code>` by @LinkOut. 👨‍💻"
