# PyQuiz

A simple quiz creation and management tool.

The purpose of this application is to allow the "quizmaster" to create custom quizzes on any subject, provided that the 
quiz questions allow only yes or no answers.

QUESTIONS

When creating a new quiz, the quizmaster uses the admin interface to enter the questions for the quiz.  Optionally, the 
quizmaster may provide correct answers for each question, depending on the type of quiz being created.

In their simplest form, questions are simply text that asks a question; however, the quiz system is flexible enough to 
allow various types of media as "prompts" (questions) for the quizzee, e.g. images, embedded video or audio clips, etc.
 
INSTRUCTIONAL MATERIAL

The quizmaster may provide specific instructional material related to the quiz subject-matter. This information will be 
used by "quizzees" as study material in preparation for taking the actual quiz.  Instructional material is optional and
may depend on the quiz type, so it is entirely left to the quizmaster's discretion whether or not to provide it.

QUIZ TYPES

A "fact" quiz is a quiz that has answers with definitive yes/no answers based on known facts, possibly including those 
facts provided in the instructional material.  This type of quiz, therefore, would require correct answers to be entered 
by the quizmaster when the quiz is created.

An "opinion" quiz has a different intention than a fact quiz: rather than testing the quizzee's knowledge of a subject,
this type of quiz is meant to collect opinion data.  For example, this type of quiz could be used to create a basic 
Tinder-style application interface by including photos of individuals as the questions and allowing the quizzee to click
(or swipe) left or right--effectively answering yes or no--depending on their level of interest in that indivdual.  

FEEDBACK

Another optional quiz feature is "feedback" which can be added to each question by the quizmaster.  If provided, this 
feedback can be presented to the quizzee after a question is answered, e.g. to display some kind of useful message or 
additional instruction in the case of an incorrect question.


