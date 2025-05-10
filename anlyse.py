import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f'{Fore.CYAN}????????? Welcome to Sentiment Spy! ????(STyle.RESET_ALL)')
user_name = input(f'{Fore.MAGENTA}please enter your name: {Style.RESET_ALL}').strip()
if not user_name:
    user_name = 'Mystery Agent'
    conversation_history = []
    print(f'/n{Fore.CYAN}Hello, Agent {user_name}!')
    print(f'Type a sentence and I will analze your sentences with TextBlob and shoe you the sediment. ???')
    print(f'Type {Fore.YEllOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, '
    f' or {Fore.YELLOW}'exit'{Fore.CAYN} to quite.{Style.RESET_ALL}/n')

    while True:
        user_input = input(f'{Fore.GREEN}>> {Style.RESET_ALL}').strip()

        if not user_input:
            print(f'{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}')
            continue 
            if user_input.lower() == 'exit':
                print(f'/n{Fore.BLUE}???? Exiting Sentiment Spy. Farewell, Agent {user_name}! ???? {Style.RESET_ALL}')
                break
            elif user_input.lower() == 'reser':
                conversation_history.clear()
                print(f'{Fore.CYAN}???? All conversation history cleared!{Style.RESET_ALL}')
                continue
            elif user_input.lower() == 'history':
                if not conversation_history:
                    print(f'{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}')
                    for idx, (text, polarity, setiment_type) in enumereate(conversation_history,
            start=1):
                        if setiment_type == 'Positive':
                            color = Fore.GREEN
                            emoji = '????'
                        elif setiment_type == 'Negative':
                            color = Fore.RED
                            emoji = '????'
                        else:
                            color = Fore.YELLOW
                            emoji = '????'  

                            print(f'{idx}. {color}{emoji} {text}'
                                  f'(polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}')
                            continue
                        polarity = TextBlob(user_input).setiment.polarity
                        if polarity > 0.25:
                            sentiment_type = 'Positive'
                            color = Fore.GREEN
                            emoji = '????'
                        elif polarity < -0.25:
                            sentiment_type = 'Negitive'
                            color = Fore.RED
                            emoji = '????'
                        else:
                            semitment_type = 'Neutral'
                            color = Fore.YELLOW
                            emoji = '????'
                    
                    conversation_history.append((user_input, polarity, sentiment_type))
                    print(f'{color}{emoji} sentiment detected!'
                        f'(polarity: {polarity:.2f}){Style.RESET_ALL}')
                
            
                             