# Pikachu Volleyball

This environment is based on the original [gym-pikachu-volleyball environment](https://github.com/HoseongLee/gym-pikachu-volleyball) and has been extended and modified to create a customized version in order to train by reinforcement learning. 

The main changes to the environment include:
* Use `gymnasium` instead of `gym`
* Add three different variations to environment
  * Normal Version: An original implementation of pikachu-volleyball 
  * Random Version: Similar with original version, except that the serve point and ball speed are randomly initialized.
  * Pixel Version: The observation state is pixels
* Implement default computer's policy


Pikachu Volleyball (対戦ぴかちゅ～　ﾋﾞｰﾁﾊﾞﾚｰ編) is an old Windows game which was developed by
"(C) SACHI SOFT / SAWAYAKAN Programmers" and "(C) Satoshi Takenouchi" in 1997.

This is an OpenAI gym environment of the game created by translating
a [reversed-engineered JavaScript version](https://github.com/gorisanson/pikachu-volleyball)
by [gorisanson](https://github.com/gorisanson) to python.