# Bandila Firebase Template Repository

### How to set up
0. Create new repository from this repo
1. clone the repository locally `git clone https://github.com/Bandila-Web-Services/Project-Boiler-Plate.git`
2. `npm install`
3. login to Firebase on team account `firebase login:ci`. Upon logging in, you will receive a token that will be used in the inside the new project's github secrets
4. login to the firebase console and in the hosting section set up the new webapp that aligns with the main project-name
5. go into the `.github/workflows/main.yaml` and `src/firebase.json` and add the project name and site name respectively
6. create a staging branch and push