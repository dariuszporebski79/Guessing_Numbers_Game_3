from flask import Flask

app = Flask(__name__)

# computer_choice = random.randint(0, 100)


@app.route('/', methods=['POST', 'GET'])
def numbers_guessing():
    form = """
        <form action="/" method="POST">
            <p> Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w maksymalnie 10 próbach </p>
            <input type="button" value="zgadłeś" />
            <input type="button" value="za dużo" />
            <input type="button" value="za mało" />
        </form>
        """
    return form



    # min = 0
    # max = 1000
    # answer = 0
    # while answer != "zgadłeś":
    #     guess = int((max-min) / 2) + min
    #     print("Zgaduję :-) ;-): ", guess)
    #     while True:
    #         answer = input("Wpisz \"za dużo\" lub \"za mało\" lub \"zgadłeś\" :-) ")
    #         if answer == "zgadłeś":
    #             print("Wygrałem :-)")
    #             break
    #         elif answer == "za dużo":
    #             max = guess
    #             break
    #         elif answer == "za mało":
    #             min = guess
    #             break
    #         else:
    #             print("Pomyliłeś się lub oszukujesz ;-)")



# ********************************
# print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w maksymalnie 10 próbach")
# min = 0
# max = 1000
# answer = 0
# while answer != "zgadłeś":
#     guess = int((max-min) / 2) + min
#     print("Zgaduję :-) ;-): ", guess)
#     while True:
#         answer = input("Wpisz \"za dużo\" lub \"za mało\" lub \"zgadłeś\" :-) ")
#         if answer == "zgadłeś":
#             print("Wygrałem :-)")
#             break
#         elif answer == "za dużo":
#             max = guess
#             break
#         elif answer == "za mało":
#             min = guess
#             break
#         else:
#             print("Pomyliłeś się lub oszukujesz ;-)")



if __name__ == '__main__':
    app.run(debug=True)
