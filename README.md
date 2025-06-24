# Animal Rescue Quest


---

## Project Overview

Animal Rescue Quest is an educational and interactive game designed to raise awareness about wildlife conservation. Players navigate through engaging maze challenges to rescue endangered animals, encountering scenarios that highlight real-world threats and conservation efforts.

## Objectives

* Promote wildlife conservation and the importance of ecological balance.
* Educate players about the threats animals face, such as habitat loss, poaching, and climate change.
* Inspire empathy and proactive conservation efforts through interactive gameplay.

## Gameplay and Features

### Main Interface

* **Captivating Play Window:** Engaging visuals and background music to immerse players.
* **Interactive Buttons:** Choose animals, watch educational films, and encounter hunters.

### Game Levels and Scenarios

#### Level 1: Jungle Expedition

* Navigate a maze, avoiding hunters and predators.
* Collect veterinary documents to score points.
* Lose by encountering poachers, triggering progression to subsequent challenges.

#### Level 2: Hunter Interaction Game

* Strategic tile-based navigation toward the magical "Kalpavriksh" tree.
* Manage animal health through hydration and nutrition.
* Navigate around cliffs, wild animals, and poachers.

#### Level 3: City Challenge

* Guide "Oreo," an injured puppy, through a maze to reach a veterinary hospital.
* Culminates in celebratory feedback emphasizing compassion and success.

## Technical Implementation

### Tools and Libraries

* **Pygame:** User interface, event handling, graphics rendering, and audio playback.
* **moviepy.editor:** Video integration and playback within the game interface.
* **pygame.mixer:** Audio playback for immersive background music.
* **Subprocess Module:** Handling external script execution for enhanced functionalities.

### Design Choices

* **Dynamic Content Rendering:** Scalable and interactive UI elements, multimedia integration.
* **Interactive Gameplay:** Collision detection, scoring, and real-time feedback.
* **Maze Generation:** Utilizes Kruskal’s algorithm for dynamic and random maze creation, ensuring unique playthroughs each time.

### Key Features

* **Character Selection:** Choose animals like Bambi deer or Donut bird, with thematic introductory videos.
* **Navigation and Controls:** Intuitive UI with Next, Back, Replay, and Quit buttons. Keyboard-based controls for gameplay.
* **Scoring and Feedback:** Real-time scoring, interactive feedback, and progression milestones.

## Gameplay Mechanics

* **Collision Detection:** Effective management of player-obstacle interactions.
* **Maze Challenges:** Strategically navigate maze layouts generated dynamically for each session.

## Metrics and Evaluation

* Real-time scoring and feedback to gauge player success.
* Encouragement messages and options to replay or continue after challenges.

## Project Structure and Usage

* Python-based game leveraging Pygame, moviepy, and subprocess modules.
* Run the game script to start interactive sessions:

  ```bash
  python main.py
  ```

---

## Conclusion

Animal Rescue Quest aims to not only entertain but also educate and inspire players to actively participate in conservation efforts, fostering a greater sense of empathy and responsibility towards wildlife.

---

**Thank You for Playing and Supporting Wildlife Conservation!**
