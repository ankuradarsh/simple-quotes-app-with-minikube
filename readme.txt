python app.py

if docker build -t quote .

than docker run -it quote || docker run quote

if docker build -t quote:0.0.1 . 

than docker run -p 5000:5000 quote || docker run -d -p 5000:5000  quote

docker tag quote:0.0.1 ankuradarsh/quotes:0.0.1

docker push ankuradarsh/quotes:0.0.1

docker run -p 5000:5000 ankuradarsh/quotes:0.0.1

minikube start (to check version i.e. minikube version)

kubectl apply -f deployment.yaml

kubectl expose deployment quotes --type=NodePort --port=5000 

minikube service quotes
output : 
W0220 23:13:50.004996   18552 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\ANKURADARSH\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
|-----------|--------|-------------|---------------------------|
| NAMESPACE |  NAME  | TARGET PORT |            URL            |
|-----------|--------|-------------|---------------------------|
| default   | quotes |       5000  | http://192.168.49.2:31628 |
|-----------|--------|-------------|---------------------------|
🏃  Starting tunnel for service quotes.
|-----------|--------|-------------|------------------------|
| NAMESPACE |  NAME  | TARGET PORT |          URL           |
|-----------|--------|-------------|------------------------|
| default   | quotes |             | http://127.0.0.1:52275 |
|-----------|--------|-------------|------------------------|
🎉  Opening service default/quotes in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.