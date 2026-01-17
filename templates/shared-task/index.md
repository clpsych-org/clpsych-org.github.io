---
title: Shared Task 2026
---

## CLPsych 2026 Shared Task: Capturing and Characterizing Mental Health Changes through Social Media Timeline Dynamics

**Overview**  
The CLPsych 2026 Shared Task builds on the longitudinal modeling paradigm introduced in CLPsych ([2022](https://aclanthology.org/volumes/2022.clpsych-1/), [2025](https://aclanthology.org/2025.clpsych-1.16.pdf)), which focused on detecting changes in individuals’ mental states and well-being, as reflected in social media timelines. The 2026 task further advances this line of work by integrating **dynamic mental health modeling**, emphasizing the identification of key self-state elements leading up to mental state changes over time.

Participants will analyze temporally ordered sequences of social media posts to characterize detailed psychological processes, key changes, as well as the interplay of such self-state processes leading up to the changes. The task builds on the CLPsych 2025 task which was grounded in the **MIND framework** (Atzil-Slonim, 2024\) that conceptualizes self-states as combinations of **Affect, Behavior, Cognition, and Desire (ABCD)** components enabling the modeling of adaptive and maladaptive self-states over time. Specifically, this year’s task aims to further explore the fine-grained elements contributing to changes. The core objective of the shared task is to develop computational models that can **identify adaptive and maladaptive self-state dimensions as well as changes over time across social media timelines aiming to characterize and summarize self-state sequences leading to such changes**.

**Task Description**  
Participants will develop systems that emulate a structured human annotation process to model mental health dynamics over time. Specifically, systems will be evaluated on their ability to:

* Predict adaptive and maladaptive **ABCD element combinations** for each individual post**. (See Table 1\) (See Example 1\)**.  
* Identify **moments of change** in mental health social media trajectories using longitudinal signals.  
* Generate concise, interpretable self-state summaries leveraging the identified  ABCD elements and contextual information leading up to changes in the user timeline.

**Annotation Framework: The MIND Model**  
Self-states are conceptualized as structured combinations of the following components:

* **Affect (A):** Emotional tone or mood.  
* **Behavior toward Self (BS)** and **Behavior toward Others (BO):** Actions or tendencies directed inward or outward.  
* **Cognition toward Self (CS)** and **Cognition toward Others (CO):** Beliefs, interpretations, and appraisals.  
* **Desire (D):** Motivations, needs, wishes, and expectations.

A **self-state** reflects a dominant mode of experiencing the self and others at a particular moment in time. At any given point, one self-state may be more dominant, shaping emotions, thoughts, motivations, and behaviors, while other self-states remain in the background and still exert subtler influence. Individuals differ in self-state flexibility—namely, their capacity to shift between self-states and sustain internal dialogue among them rather than becoming stuck in a rigid dominant state. Some self-states are more **adaptive** and support well-being, whereas others are more **maladaptive** and involve negative feedback loops, or self–other conflict. Self-states are dynamic: they fluctuate across time and context, and shifts in dominance and transitions between states may signal meaningful **change** in mental health.

Modeling these transitions is central to the CLPsych 2026 task. Below is the ABCD Elements Table with Adaptive and Maladaptive Examples.

**Table 1: ABCD Elements Table with Adaptive and Maladaptive Examples:**

<style>
    #table1 {
         border-collapse: collapse;
     }
    #table1 td, #table1 th {
        border: 1px solid black !important;
        vertical-align: top;
        padding: 2px;
    }
</style>

<table id="table1">
  <thead>
    <tr>
      <th colspan="2">Dimension</th>
      <th colspan="2">Sub-Categories</th>
    </tr>
    <tr>
      <th colspan="2"><strong>ABCDDimension</strong> <strong>Explanation</strong></th>
      <th><strong>Adaptive Examples</strong></th>
      <th><strong>Maladaptive Examples</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Affect</strong></td>
      <td>Type of emotion expressed by a person</td>
      <td>
        Calm/Laid back; Emotional pain/Grieving; Content/Happy; Vigor/Energetic;
        Justifiable anger; Assertive anger; Proud
      </td>
      <td>
        Anxious/Tense/Fearful; Depressed/Desperate/Hopeless; Mania;
        Apathetic/Don’t care/Blunted; Angry (Aggressive, Disgust, Contempt);
        Ashamed/Guilty
      </td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Behavior</strong></td>
      <td>
        <em><strong>Behavior of the self with the Other (BO):</strong></em>
        The person’s main behavior(s) toward the other
      </td>
      <td>
        Relating behavior; Autonomous behavior, approach behavior
      </td>
      <td>
        Fight or flight behavior; avoidance, Overcontrolled/Controlling behavior
      </td>
    </tr>
    <tr>
      <td>
        <em><strong>Behavior toward the Self(BS):</strong></em>
        The person’s main behavior(s) toward the self
      </td>
      <td>
        Self-care behavior, self-improvement
      </td>
      <td>
        Self-harm; Neglect; Avoidance behavior, self-sabotage
      </td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Cognition</strong></td>
      <td>
        <em><strong>Cognition of the Other(CO):</strong></em>
        The person’s main perceptions of the other
      </td>
      <td>
        Perception of the other as related;
        Perception of the other as facilitating autonomy needs
      </td>
      <td>
        Perception of the other as detached or over-attached;
        Perception of the other as blocking autonomy needs
      </td>
    </tr>
    <tr>
      <td>
        <em><strong>Cognition of the Self (CS):</strong></em>
        The person’s main self-perceptions
      </td>
      <td>
        Self-acceptance; Self-compassion, self-esteem
      </td>
      <td>
        Self-criticism, lack of self-confidence, lack of self-identity
      </td>
    </tr>
    <tr>
      <td><strong>Desire</strong></td>
      <td>
        The person's main desire, need, intention, fear or expectation.
      </td>
      <td>
        Relatedness needs; Autonomy and adaptive control needs; Competence needs
      </td>
      <td>
        Expectation that relatedness needs will not be met;
        Expectation that autonomy needs will not be met;
        Expectation that competence needs will not be met
      </td>
    </tr>
  </tbody>
</table>

**Example 1: Annotated Example of ABCD Element Combinations:**

<pre style="line-height: 1;">
{  
  "post": "Heavy and uneasy. A significant date for someone close is approaching, yet my mind keeps drifting toward wanting to vanish from everything. I stay because the thought of causing her pain stops me. Inside, there’s a sense of numb distance, like I’m disconnected from myself and others.",  
  "evidence": {  
    "adaptive-state": {  
      "C-O": {  
        "Category": "(1) Perception of the other as related",  
        "highlighted_evidence": "the thought of causing her pain stops me"  
      }  
    },  
    "maladaptive-state": {  
      "A": {  
        "Category": "(12) Ashamed, guilty",  
        "highlighted_evidence": "Heavy and uneasy"  
      },  
      "C-S": {  
        "Category": "(2) Self criticism",  
        "highlighted_evidence": "there’s a sense of numb distance, like I’m disconnected from myself and others"  
      },  
      "D": {  
        "Category": "(6) Expectation that competence needs will not be met",  
        "highlighted_evidence": "my mind keeps drifting toward wanting to vanish from everything"  
      }  
    }  
  }  
}
</pre>

**Evaluation**  
Submissions will be evaluated on their ability to:

* Accurately predict ABCD components: their adaptive/maladaptive self-state subcategories.  
* Detect changes in longitudinal timelines evaluated on a post and on a timeline-level.  
* Generate coherent self-state summaries leading up to user changes grounded on ABCD elements and reflecting mental health dynamics .

**CLPsych 2026 Timeline**

* Registration deadline (**Feb 15**)  
* Receiving guidelines on accessing sample data (**Mar 1**)  
* Receiving instructions on the task and training data (**Mar 11**)   
* System submissions on test set **(Apr 18\)**  
* Shared Task Paper submissions **(May 1\)**  
* Camera-ready papers due **(May 15\)**

**How to Participate**  
Teams must complete:

* **One [team registration form](https://docs.google.com/forms/d/e/1FAIpQLSdKp0JeE9CfBd59gFGF9YePKEFC6JXmKC8wd383syoGNtX7fw/viewform?usp=dialog)**, and  
* **One [individual registration form](https://docs.google.com/forms/d/e/1FAIpQLSftD9EbFFHMW_canwvXBYk87va6snnkpX9CglQl6GhAO1aDjQ/viewform?usp=dialog) per team member**.

Researchers seeking collaborators are encouraged to contact the organizers.

**Organizers**

* Iqra Ali (Queen Mary University of London)  
* Talia Tseriotou (Queen Mary University of London)  
* Yuxiang Zhou (Queen Mary University of London)  
* Dana Atzil-Slonim (Bar-Ilan University)  
* Guy Dvir (Bar-Ilan University)  
* Ayal Klein (Ariel University)  
* Aya Shamir (Bar-Ilan University)  
* Dan Sayda (Bar-Ilan University)  
* Ayah Zirikly (George Washington University)  
* Maria Liakata (Queen Mary University of London & The Alan Turing Institute)

**Contact**  
📧 [**clpsych-2026-shared-task@googlegroups.com**](mailto:clpsych-2026-shared-task@googlegroups.com)

**References**

* Tseriotou, T., Chim, J., Klein, A., Shamir, A., Dvir, G., Ali, I., Kennedy, C., Kohli, G. S., Hills, A., Zirikly, A., Atzil-Slonim, D., & Liakata, M. (2025). Overview of the CLPsych 2025 shared task: Capturing mental health dynamics from social media timelines.  
* Atzil-Slonim, D. (2025). Multimodal Intrapersonal and Interpersonal Dynamics (MIND): A Transtheoretical Coding Manual. [https://osf.io/d5m2x/files/znbfx](https://osf.io/d5m2x/files/znbfx)  
* Atzil-Slonim, D. (2026). Leveraging theoretical and technological innovations to study the mechanisms that underlie therapeutic change in psychotherapy. In L. Castonguay, D. Atzil-Slonim, M. Barkham, & W. Lutz, (Eds). Practice-Based Evidence in the Psychological Therapies: Towards Clinical, Training, and Public Policy Guidelines. Oxford University Press, UK.  
* Tsakalidis, A., Chim, J., Bilal, I. M., & Zirikly, A. (2022). Overview of the CLPsych 2022 shared task: Capturing moments of change in longitudinal user posts.

**Information on previous shared tasks is available for [2021](https://clpsych.org/shared-task/2021), [2022](https://clpsych.org/shared-task/2022)**,[**2024**](https://clpsych.org/shared-task/2024) **and [2025](https://clpsych.org/), and papers and presentations from previous workshops are available on the ACL anthology ([2022](https://aclanthology.org/volumes/2022.clpsych-1/), [2024](https://aclanthology.org/volumes/2024.clpsych-1/), [2025](https://aclanthology.org/2025.clpsych-1.16.pdf)).**
