# Week 11 answers

## Exercise 1
1. The message the customer never saw:
2. How many times the customer has spoken:
3. Can the model tell that the last reply came from the order tool? Why does that matter?
4. The customer now types "thanks". How many messages are sent on the next call?

1. The message the customer never saw: the system message, which holds the instructions
2. How many times the customer has spoken: twice
3. No. In the history every reply has the role assistant, whether a rule, a tool, or the
   model wrote it. The model reads the whole history, so it can copy the pattern of an
   earlier tool answer and state something the tool never said.
4. Six: the five messages above plus the new user message

The chatbot only goes by what it is recently told, we tested this and it had a 100% success rate. Ideally, stuff like order status, price, stocks should be from data not a chatbot. The mistake could be that adding instructions can only cover up a problem instead of outright fixing it. 