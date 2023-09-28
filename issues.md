<div align="center">



<img src="assets/media/documentation/issues-icon.svg" width=200>


# Python Issues and Bugs<!-- omit in toc -->

</div>

## Table of Contents<!-- omit in toc -->
- [1. Code Structure Issues](#1-code-structure-issues)
  - [1.1 Cannot access OpenTrivia DB for Tech, Art and Maths.](#11-cannot-access-opentrivia-db-for-tech-art-and-maths)


# 1. Code Structure Issues

## 1.1 Cannot access OpenTrivia DB for Tech, Art and Maths.
<div align=center><details><summary><b> click here to view the issue output</summary></b>

![](assets/media/issues/2023-09-24-18-11-18.png)
</details></div>

Under "Now on to Art!" and "Now on to Math!" it should reveal the quiz. Should also work for an earlier technology section.

It works for Science and English.

This is likely because the OpenTrivia DB API not active for the specific category.

Removed Easy difficulty.
![](assets/media/issues/2023-09-28-09-22-52.png)


<div align=center><details><summary><b> click here to view the solution output</summary></b>

![](assets/media/issues/2023-09-28-09-24-22.png)

![](assets/media/issues/2023-09-28-09-24-51.png)

![](assets/media/issues/2023-09-28-09-25-13.png)

![](assets/media/issues/2023-09-28-09-25-39.png)

here's the second attempt: we can see that the quiz is shuffling questions,making it exciting for the user.

![](assets/media/issues/2023-09-28-09-29-17.png)

</div></details>

In long term, best solution would be to migrate to local JSON database, as json files are saved.
