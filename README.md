# KCB-Public A Python API to interact with bep-20 tokens on the binance smart chain

Tools needed:
+ BSC scan API keys
+ Metamask wallet address
+ wallet address private key


This project is a high level terminal to interact with tokens that use pancakeswap


        Info Functions:                Describtion:

        c:                   returns current connected contract
        ntoken:              (address) function to change the current contract aka add a new token and replace old one
        cinfo:               information on token
        methods:             returns all methods of token
        winfo:               (wallet_address) information of the wallet
        gas:                 gas ? gives you current gas. gas (any number) set a new gas. default is 5
        scams:               see examples of scam tokens
        stest:               test if scam filter are working

        Trading Functions:

        *type                buy and sell can be manual (press enter to send) or auto
        t: -Do not use-      (from, to, amount(int or "max"), type("manual" or "auto")) transfer tokens between wallets
        buy:                 (buyer, amount, type) buys amount of tokens at the price of the block it enters
        sell:                (seller, amount or "max", type) sells amount of tokens
        a:                   (wallet) approves a token to sell
        snipe:               (buyer, amount, contract_address) snipe fair launches by connecting to to contract and sending a buy at market price and approving
        mbuy:                (wallet, amount, how many times, contract) snipes a new contract and buys the amount the times you tell it
        msell:               (wallet, amount) it sells amount until wallet tokens are 0

        System Functions:

        r:                   restarts the application
        logs:                see all logs
  

![kcbbiot](https://user-images.githubusercontent.com/63566185/128554755-6e404973-c878-4e7f-9f0c-57dc50bada36.JPG)
