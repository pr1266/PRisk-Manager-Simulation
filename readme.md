# Margin-Call Proof Risk Manager
Risk management is one of the important parts of trading.
Nowadays, algorithmic trading helping us to manage our risk per trade automaticly
But there is a hard challenge, 
How much risk should be considered in each trade?
This is what we discuss about, we implemented an algorithm that guarantees that margin call never treat your account.


## About Project
Main idea of this algorithm inspired of TCP/IP Congestion control
When there is a certain number of packet loss in connection, sender reduces window size to half
and when there is a consecutive acks, sender increases the window size to 2x
We proposed an algorithm similar to congestion control to avoid major losses in out trades
And it is proved that in this case, if all trades hit stop loss, it doesn't matter because the overall is limited
and there is no margin call threat for our balance. you may ask how?
Here is the point. If we start out trading with 1% of our balance per trade, and
reduce it to half after 4 stop loss, or increase it after 16 rewards. Try it !
Remember it's a Python simulation of original algorithm and you must implement it by your need in Pine or MQL4/5

## How to run project?
Just run this two commands in your terminal/prompt:
```
pip install requirements.txt
python main.py
```

## Contact

* ![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) pour.pourya1999@gmail.com
* [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/pr1266/)

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.