# Basisproject (API Development)
Voor het eerste deel van het project moest er een API gemaakt worden rond een zelfgekozen thema. Deze API moest via docker opgestart worden en gehost worden via Okteto ook moest er een front-end aangekoppeld worden.

# Thema
Ik heb gekozen om met het thema bier te werken. Ik heb hiervoor gekozen zodat ik all mij gedronken bieren hier bij kan houden.

# API 
De API is vrij basis er zitten 4 funcites in:
  - GET request 1: deze laat alle bieren zien die in de database zitten.
  - GET request 2: deze laat de namen van bieren uit een bepaalde brouwerij zien die in de database zitten.
  - GET request 3: deze laat alle bieren zien die in de database zitten maar gerangschik per soort.
  - POST request: voeg een nieuw bier + al de gegevens over het bier toe aan de database.

# Front-end
In mijn front-end roep ik al mijn GET funcites op met verschillende knoppen. Ook is er een formulier voorzien waarmee een nieuwe bier kan toevoegd worden via de POST funcite.

De webpage word gestyled met css en met bootstrap. Er is ook een javascript die ervoor zorgt dat de pagina overzichtelijk blijft.
![image](https://user-images.githubusercontent.com/71765408/202700920-a8b27d22-3fa8-4875-9d85-668773860e5c.png)

# Postman screenshots
# GET request 1
![image](https://user-images.githubusercontent.com/71765408/202702782-ec6f4ad1-65d9-451c-bf5d-190967f4a0ac.png)


# GET request 2
![image](https://user-images.githubusercontent.com/71765408/202703001-b6a38f25-1c36-4913-8a32-f2a2ac41e3eb.png)


# GET request 3
![image](https://user-images.githubusercontent.com/71765408/202703208-e05a7008-3aed-47bc-aa1d-0667e8cd1bdb.png)


# POST request
![image](https://user-images.githubusercontent.com/71765408/202704359-33d2db48-dfe1-485f-b2ab-de286462be15.png)


# OpenAPI docs screenshots
![image](https://user-images.githubusercontent.com/71765408/202705453-8afccdf6-88a6-4bcd-ae0d-cf95753da5ce.png)
![image](https://user-images.githubusercontent.com/71765408/202705518-dc762de3-5c68-46ef-93e1-ec2fc27ee999.png)
![image](https://user-images.githubusercontent.com/71765408/202705591-e17fa9ca-566a-4531-b788-ceb1ae50419a.png)
![image](https://user-images.githubusercontent.com/71765408/202705653-a141a47f-38e8-444b-b823-6fdd26ec8002.png)

# Links
- Hosted API: https://bier-service-joppevdb.cloud.okteto.net
- Front-end repo: https://github.com/joppevdb/joppvdb.github.io.git
- Hosted front-end: https://joppevdb.github.io/joppvdb.github.io/
