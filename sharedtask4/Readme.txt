Prequiste:
Tensorflow
G2ptoolkit

https://github.com/cmusphinx/g2p-seq2seq


Preprocessing:
1)Converted each sentence to a sentence containing lowercase letters and storing them.
Ex:​ ​ paYcan​ ​ ratna​ ​ muKya​ ​ ca​ ​ uparatna​ ​ catuzwaya​ ​ → ​ ​ paycan​ ​ ratna​ ​ mukya​ ​ ca​ ​ uparatna
​ Catuzwaya
2. Created a training test file with each line containing words in lowercase and
corresponding​ ​ uppercase​ ​ space​ ​ separated​ ​ letters.
Ex:
suramfttika​ ​ s ​ ​ u ​ ​ r ​ ​ a ​ ​ m ​ ​ f ​ ​ t ​ ​ t ​ ​ i ​ ​ k ​ ​ A
​3.​ ​ ​ Clean​ ​ training​ ​ and​ ​ test​ ​ data​ ​ to​ ​ remove​ ​ erroneous​ ​ words​ ​ like​ ​ words​ ​ containing​ ​ non​ ​ ascii
characters​ ​ etc.

Train​ ​ the​ ​ model​ ​ using​ ​ following​ ​ command​ ​ :
g2p-seq2seq​ ​ --train​ ​ train.dict​ ​ --model​ ​ model_folder_path

Evaluate​ ​ on​ ​ the​ ​ test​ ​ data​ ​ using​ ​ following​ ​ command:
g2p-seq2seq​ ​ --evaluate​ ​ test.dict​ ​ --model​ ​ model_folder_path
