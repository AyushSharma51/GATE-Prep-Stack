--
-- PostgreSQL database dump
--

\restrict je8UsEs5l6fdOImn01VoMGtSyB9hYeoWaUupjcsgye5bRVutQFF68I96q7V21dd

-- Dumped from database version 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alembic_version (version_num) FROM stdin;
750844a84b74
\.


--
-- Data for Name: branches; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.branches (id, name, is_deleted) FROM stdin;
24947b83-13d6-4ff8-b42d-fadcf1876b91	cse	f
f0e9eb93-0de1-4886-88d9-d5bdb142702d	da	f
b7840362-d296-4496-9de5-079c5e5bb736	me	f
\.


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.subjects (id, name, branch_id, is_deleted) FROM stdin;
49c82e3e-c5a2-44c7-823b-b69c33560d8c	compiler design	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
553dd23d-9091-4ba7-a892-d487101e9325	operating system	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
c5e1f1bd-f357-4c71-a9e7-4eb0590297c6	digital logic	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
643ec3ca-0a2b-4035-b165-0277b4c619b8	computer networks	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
55f813b0-ff62-4639-8d1c-38526a0d465e	theory of computation	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
22b1527f-3171-44b3-8272-9491ca5fb680	dbms	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
352424c7-5f9e-4608-a0f9-1ec5ef4240ab	general aptitude	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
fef6be72-f588-4c0a-be8b-5ef81a81a11d	engineering mathematics	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
a88feaca-67e3-4834-b72c-ae4879642f65	computer organization and architecture	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
67d5a2bf-b4e0-4ea8-bb58-79cbc6204780	programming and data structures	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
8d14e93e-bfe1-42ab-93d1-d6be31e5f9b4	algorithms	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
8585a086-e79e-488b-978d-b00d535fe208	discrete mathematics	24947b83-13d6-4ff8-b42d-fadcf1876b91	f
\.


--
-- Data for Name: tests; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.tests (id, subject_id) FROM stdin;
78b403d4-e680-467f-892e-09014e5ed9d5	8d14e93e-bfe1-42ab-93d1-d6be31e5f9b4
2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	8d14e93e-bfe1-42ab-93d1-d6be31e5f9b4
58e11b13-6d43-49d0-9d25-d39c75c8544a	352424c7-5f9e-4608-a0f9-1ec5ef4240ab
fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	c5e1f1bd-f357-4c71-a9e7-4eb0590297c6
3c89fe14-a21c-4850-81e8-66e9d66d7f9f	8d14e93e-bfe1-42ab-93d1-d6be31e5f9b4
7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	fef6be72-f588-4c0a-be8b-5ef81a81a11d
d8952437-3b57-4e50-aa0a-58450faabbe7	8d14e93e-bfe1-42ab-93d1-d6be31e5f9b4
cd85a117-60c2-4b20-97da-f54a9ade7349	8d14e93e-bfe1-42ab-93d1-d6be31e5f9b4
97307c87-09f5-4ea9-b998-f4df904b8e0c	67d5a2bf-b4e0-4ea8-bb58-79cbc6204780
d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	55f813b0-ff62-4639-8d1c-38526a0d465e
6b680e6e-88ba-4429-9d35-cb793ee99891	49c82e3e-c5a2-44c7-823b-b69c33560d8c
d01b497b-5f8c-4880-8e6d-19dc66fd82bd	49c82e3e-c5a2-44c7-823b-b69c33560d8c
a19a588f-7078-4453-ae2d-665e731164cc	49c82e3e-c5a2-44c7-823b-b69c33560d8c
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.questions (id, test_id, question_text, question_type, numerical_answer, tolerance, marks) FROM stdin;
d2fdde2e-258a-42e0-aed4-42052202d787	78b403d4-e680-467f-892e-09014e5ed9d5	A graph has 8 vertices and 12 edges. The maximum number of edges in a spanning tree of this graph is	mcq	\N	\N	1
71c52cf4-2fe9-4742-89ad-64945f566170	78b403d4-e680-467f-892e-09014e5ed9d5	The time complexity of the following algorithm: for (i = 1; i <= n; i++) { for (j = 1; j <= i; j++) { printf("*"); } } is	mcq	\N	\N	2
53b0fb59-9a9d-4e8a-8ac6-e95eab348a07	78b403d4-e680-467f-892e-09014e5ed9d5	Which of the following sorting algorithms has the lowest worst-case time complexity?	mcq	\N	\N	1
b3f21eea-232e-4e70-8ef7-3bf665df7517	78b403d4-e680-467f-892e-09014e5ed9d5	The number of possible min-heaps that can be constructed from the elements {1, 2, 3, 4, 5, 6, 7} is	nat	64	\N	2
a36bce66-5a4b-4c15-a48a-8b67c8e75e43	78b403d4-e680-467f-892e-09014e5ed9d5	Consider the following recurrence relation: T(n) = 2T(n/2) + n. The value of T(16) is	nat	80	\N	1
dc8d66f0-f40e-49bb-8d79-3c49b12d9669	78b403d4-e680-467f-892e-09014e5ed9d5	Which of the following data structures can be used for efficient implementation of recursion?	msq	\N	\N	2
36e3ca52-f8cc-46b8-bc8d-f875f99ff428	78b403d4-e680-467f-892e-09014e5ed9d5	The time complexity of the following algorithm: for (i = 1; i <= n; i++) { for (j = 1; j <= n; j++) { printf("*"); } } is	mcq	\N	\N	1
23422be1-f8e4-4e17-9ea8-03d49b101b25	78b403d4-e680-467f-892e-09014e5ed9d5	Consider a binary search tree with the following properties: (i) All leaves are at the same level. (ii) All internal nodes have two children. The height of the tree is	nat	4	\N	2
34d82888-578d-48ec-8155-7ab223d2c365	78b403d4-e680-467f-892e-09014e5ed9d5	Which of the following algorithms can be used for finding the shortest path in a weighted graph?	msq	\N	\N	1
3932836f-fd4e-469e-ba1a-79904aad2d7f	78b403d4-e680-467f-892e-09014e5ed9d5	The time complexity of the merge sort algorithm is	mcq	\N	\N	2
461d8b14-b13c-44fd-b69d-2fffeb2f4933	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	Consider a hash table with 10 slots, and a hash function that maps each key to one of the slots. If 5 keys are inserted into the table, what is the expected number of collisions?	nat	1.25	\N	2
f55db56b-7033-407b-a03d-1b74697b3097	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	What is the time complexity of the following algorithm: for i in range(n): for j in range(i+1, n): print(i, j)	mcq	\N	\N	1
28dc92ad-6964-411e-b89d-ca1e075c5edb	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	A binary search tree has the following property: for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. Which of the following operations can be performed in O(log n) time?	msq	\N	\N	2
94665d33-f79f-45cf-b5e5-99719fc6de77	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	A graph has 10 vertices and 12 edges. What is the maximum number of spanning trees that can be formed from this graph?	nat	16	\N	2
a75fb4da-4b2b-4540-b7d2-d13d0a82aa85	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	Consider a sorting algorithm that uses a divide-and-conquer approach. If the algorithm takes 10 seconds to sort 1000 elements, how long will it take to sort 4000 elements?	mcq	\N	\N	1
4df0415e-cf5d-4d1f-89c5-aa553c051875	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	A dynamic programming algorithm is used to solve a problem with the following recurrence relation: T(n) = 2T(n/2) + n. What is the time complexity of this algorithm?	mcq	\N	\N	2
abb6da13-f02e-49e0-baab-ad0236cb6641	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	A queue is implemented using a linked list. Which of the following operations can be performed in O(1) time?	msq	\N	\N	1
966df665-e0da-465d-a7a1-d5fef9327b6c	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	A string matching algorithm is used to find all occurrences of a pattern in a text. If the pattern has a length of 10 and the text has a length of 100, what is the maximum number of comparisons required to find all occurrences of the pattern?	nat	91	\N	2
a1af9a53-2049-4001-a4df-74efdd5bc1c8	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	Consider a graph with 10 vertices and 15 edges. Which of the following algorithms can be used to find the minimum spanning tree of this graph?	mcq	\N	\N	1
da6c75f1-b80e-4ac2-ab32-04af44be471b	2cbef8d2-99e3-4ac9-96dc-a422fd94f98f	A recursive algorithm is used to solve a problem with the following recurrence relation: T(n) = T(n-1) + n. What is the time complexity of this algorithm?	mcq	\N	\N	2
5cc39816-f8ae-426e-89df-644720b1298b	58e11b13-6d43-49d0-9d25-d39c75c8544a	A snail is at the bottom of a 20 feet deep well. Each day, it climbs up 3 feet, but at night, it slips back 2 feet. How many days will it take for the snail to reach the top of the well?	nat	18	\N	2
2cf38472-2ee8-4d40-aac4-f1004626937f	58e11b13-6d43-49d0-9d25-d39c75c8544a	The sum of two numbers is 40. The sum of their reciprocals is 1/10. What are the two numbers?	msq	\N	\N	2
e3de3c7d-25d8-485f-b38f-1f8d3481ffed	58e11b13-6d43-49d0-9d25-d39c75c8544a	A company produces 100 units of a product per day. The cost of producing x units is given by the equation C(x) = 100x + 500. The revenue from selling x units is given by the equation R(x) = 200x - 0.5x^2. What is the daily profit of the company?	nat	4950	\N	1
99ad7253-6e5c-4d45-a793-024e1cc5d179	58e11b13-6d43-49d0-9d25-d39c75c8544a	A bat and a ball together cost $1.10. The bat costs $1.00 more than the ball. How much does the ball cost?	mcq	\N	\N	1
39ef85c6-1c15-4a10-917c-70d6b7d8381e	58e11b13-6d43-49d0-9d25-d39c75c8544a	A water tank can be filled by two pipes, A and B, in 30 minutes and 45 minutes respectively. Pipe C can empty the tank in 90 minutes. If all three pipes are opened simultaneously, how long will it take to fill the tank?	nat	36	\N	2
b7c19f7a-a918-4812-b83d-33b6d5892cae	58e11b13-6d43-49d0-9d25-d39c75c8544a	A box contains 5 red balls, 3 blue balls, and 2 green balls. Which of the following statements are true?	msq	\N	\N	1
cf44fddc-e755-4edb-9a36-1d7914bc502d	58e11b13-6d43-49d0-9d25-d39c75c8544a	A car travels from city A to city B at an average speed of 60 km/h and returns at an average speed of 40 km/h. What is the average speed of the car for the entire trip?	nat	48	\N	1
60d3bb11-ea0b-4fb1-85a1-de43249f7162	58e11b13-6d43-49d0-9d25-d39c75c8544a	A company has two types of machines, A and B. Machine A produces 20 units per hour, while machine B produces 30 units per hour. The company operates machine A for 4 hours and machine B for 2 hours. What is the total production of the company?	nat	160	\N	1
d2d0a1b8-daad-4856-8fb3-f5d0e65d0081	58e11b13-6d43-49d0-9d25-d39c75c8544a	A person invests $1000 in a savings account that earns an annual interest rate of 5%. How much will the person have in the account after 2 years, assuming the interest is compounded annually?	nat	1102.5	\N	2
1bc995ea-0278-4080-a250-2446d6334af0	58e11b13-6d43-49d0-9d25-d39c75c8544a	A survey of a group of people showed that 60% of the people like coffee, 40% like tea, and 20% like both coffee and tea. What percentage of people like either coffee or tea?	mcq	\N	\N	1
b906c081-008b-4de7-b52c-d239ef02b69b	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A sequential circuit has two flip-flops A and B, two inputs X and Y, and one output Z. The state table for this circuit is given as follows: \n| A | B | X | Y | Next A | Next B | Z |\n| --- | --- | --- | --- | --- | --- | --- |\n| 0 | 0 | 0 | 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 1 | 0 | 1 | 1 |\n| 0 | 0 | 1 | 0 | 1 | 0 | 0 |\n| 0 | 0 | 1 | 1 | 1 | 1 | 1 |\n| 0 | 1 | 0 | 0 | 0 | 0 | 0 |\n| 0 | 1 | 0 | 1 | 0 | 1 | 0 |\n| 0 | 1 | 1 | 0 | 1 | 0 | 1 |\n| 0 | 1 | 1 | 1 | 1 | 1 | 0 |\n| 1 | 0 | 0 | 0 | 0 | 0 | 1 |\n| 1 | 0 | 0 | 1 | 0 | 1 | 0 |\n| 1 | 0 | 1 | 0 | 1 | 0 | 0 |\n| 1 | 0 | 1 | 1 | 1 | 1 | 1 |\n| 1 | 1 | 0 | 0 | 0 | 0 | 0 |\n| 1 | 1 | 0 | 1 | 0 | 1 | 1 |\n| 1 | 1 | 1 | 0 | 1 | 0 | 1 |\n| 1 | 1 | 1 | 1 | 1 | 1 | 0 |\nWhat is the minimum number of gates required to implement the given sequential circuit?	nat	10	\N	2
2c31ae06-e084-4298-921d-469e0d8ec6e8	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A 4-bit synchronous counter using JK flip-flops is designed to count in the sequence 0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15. What are the inputs to the first and last flip-flops?	msq	\N	\N	2
3412373f-c125-467c-9951-6596402e3386	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A digital circuit is designed using a 4-to-1 multiplexer and a 3-to-8 decoder. How many input lines are required for this circuit?	nat	6	\N	1
676101fa-67fb-41af-ba3c-96c173f8aadd	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A sequential circuit consists of two D flip-flops A and B, and one input X. The state table for this circuit is given as follows: \n| A | B | X | Next A | Next B |\n| --- | --- | --- | --- | --- |\n| 0 | 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 1 | 0 |\n| 0 | 1 | 0 | 0 | 1 |\n| 0 | 1 | 1 | 1 | 1 |\n| 1 | 0 | 0 | 0 | 0 |\n| 1 | 0 | 1 | 0 | 1 |\n| 1 | 1 | 0 | 1 | 0 |\n| 1 | 1 | 1 | 1 | 1 |\nWhat is the output of the circuit after 5 clock pulses, if the initial state is A=0, B=0, and the input sequence is X=1, 0, 1, 0, 1?	nat	11	\N	2
e72e3503-6ad5-434a-ad4f-2a114754f863	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A digital circuit is designed using two 2-to-4 decoders and one 4-to-1 multiplexer. What is the maximum number of input lines required for this circuit?	mcq	\N	\N	1
08ef09c5-0d92-4de4-a009-709eeb28a15f	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A 3-bit binary counter using T flip-flops is designed to count in the sequence 0, 1, 2, 3, 4, 5, 6, 7. What is the minimum number of gates required to implement the given counter?	nat	6	\N	2
7307fbc3-b443-4c5f-9a7b-9d7b94e346ae	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A digital circuit consists of two NAND gates and one NOR gate. The output of the first NAND gate is connected to one input of the second NAND gate, and the output of the second NAND gate is connected to one input of the NOR gate. What is the output of the circuit, if the inputs to the first NAND gate are A=1, B=0, and the input to the NOR gate is C=1?	mcq	\N	\N	1
63dedc19-b54f-4736-b99e-c1a3a6831acf	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A sequential circuit consists of two JK flip-flops A and B, and one input X. The state table for this circuit is given as follows: \n| A | B | X | Next A | Next B |\n| --- | --- | --- | --- | --- |\n| 0 | 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 1 | 0 |\n| 0 | 1 | 0 | 0 | 1 |\n| 0 | 1 | 1 | 1 | 1 |\n| 1 | 0 | 0 | 0 | 0 |\n| 1 | 0 | 1 | 0 | 1 |\n| 1 | 1 | 0 | 1 | 0 |\n| 1 | 1 | 1 | 1 | 1 |\nWhat are the next states of the circuit after 3 clock pulses, if the initial state is A=0, B=0, and the input sequence is X=1, 0, 1?	msq	\N	\N	2
b8561117-0c4e-41fe-bcc3-dcfeb523ba89	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A digital circuit is designed using a 4-to-1 multiplexer and a 3-to-8 decoder. What is the maximum number of output lines required for this circuit?	nat	8	\N	1
8015b04f-b9d4-49fa-b18a-b84a0437eb57	fa4edf24-ab74-4639-8e0f-3f4f6bf9dd86	A sequential circuit consists of two D flip-flops A and B, and one input X. The state table for this circuit is given as follows: \n| A | B | X | Next A | Next B |\n| --- | --- | --- | --- | --- |\n| 0 | 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 1 | 0 |\n| 0 | 1 | 0 | 0 | 1 |\n| 0 | 1 | 1 | 1 | 1 |\n| 1 | 0 | 0 | 0 | 0 |\n| 1 | 0 | 1 | 0 | 1 |\n| 1 | 1 | 0 | 1 | 0 |\n| 1 | 1 | 1 | 1 | 1 |\nWhat is the output of the circuit after 4 clock pulses, if the initial state is A=0, B=0, and the input sequence is X=1, 0, 1, 0?	mcq	\N	\N	2
a8fa9a4f-4f45-4418-92fa-c8fe7223ffc0	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	Consider a binary heap with 15 elements. What is the maximum height of the heap?	nat	3	\N	1
e1cc1467-6542-41b4-8474-a1eeaafe25d9	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	Which of the following algorithms has an average time complexity of O(n log n) for sorting?	mcq	\N	\N	2
b749919b-f4e3-41ca-9c14-830b612d8795	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	A graph has 8 vertices and 12 edges. What is the minimum number of colors required to color the graph such that no two adjacent vertices have the same color?	nat	3	\N	2
27a286dd-72b1-4bba-9d15-e126bc8d59f2	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	Which of the following statements are true about Dijkstra's algorithm?	msq	\N	\N	1
70f5e689-f7ed-4421-8be0-85c313e495e3	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	A matrix has 10 rows and 15 columns. What is the minimum number of operations required to find the transpose of the matrix?	nat	150	\N	1
be49b3ea-1b99-4102-94fb-51a240ad9804	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	Which of the following algorithms is used for finding the maximum flow in a flow network?	mcq	\N	\N	2
22550166-b423-4d37-b4e9-30201741110e	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	A stack has 10 elements. What is the minimum number of operations required to reverse the stack?	nat	9	\N	1
5e6c6aa8-e6ce-46a6-a12d-2b8fe4e0791a	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	Which of the following statements are true about the DFS algorithm?	msq	\N	\N	2
df5b377b-239c-436f-bc95-a817240ef52f	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	A queue has 12 elements. What is the minimum number of operations required to find the middle element of the queue?	nat	6	\N	1
3ff051d6-1a64-476f-9bb9-dbf60cb43ea0	3c89fe14-a21c-4850-81e8-66e9d66d7f9f	Which of the following algorithms has a worst-case time complexity of O(n^2) for sorting?	mcq	\N	\N	2
48cf615c-0c26-4b5f-9978-ccad7e247672	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The value of the definite integral ∫(x^2 + 3x - 4) dx from x = 0 to x = 2 is	nat	10	\N	2
6c14fb56-ece6-47d0-8429-83f5f6cf30ba	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	If the function f(x) = (x - 1)^2 is defined for all real numbers, then the value of ∫f(x) dx from x = 0 to x = 2 is	nat	2.666666666666667	\N	1
acf5cabb-37c1-44ee-9720-14230825f1f6	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The differential equation that represents the family of curves y = (A/x) + B is	mcq	\N	\N	1
4257b4b8-6ada-4355-82c3-37f7361742fc	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The function f(x) = e^(-x) is	mcq	\N	\N	1
9746ea91-eb00-410a-b37b-2286113bdbef	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The system of linear equations x + y + z = 3, x + 2y + 3z = 6, and x + 4y + 7z = 10 has	mcq	\N	\N	1
542f2dc1-93ef-4256-97af-229ba5859678	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The Fourier series of the function f(x) = |x| from x = -π to x = π is	msq	\N	\N	2
1bc7cbea-ea6a-4034-80a7-8aa65af6467c	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The Laplace transform of the function f(t) = t^2 * sin(t) is	nat	2	\N	2
b956e9c1-1e64-469b-8f54-d8a4ccb39ff8	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The function f(x) = x^3 - 6x^2 + 11x - 6 has	mcq	\N	\N	1
37ce9205-049f-4ea0-b090-5dbae2972bc3	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The value of the limit lim(x→0) [sin(x) / x] is	nat	1	\N	1
cc66ff75-46e3-4e3e-b01f-13bfe043d865	7c87ccb2-758e-4e02-894e-2ce58f7ab6d2	The function f(z) = (z^2 + 1) / (z^2 - 4) has singularities at	msq	\N	\N	2
50acb980-6d53-437a-9591-e55fab88c209	d8952437-3b57-4e50-aa0a-58450faabbe7	What is the time complexity of the algorithm that solves the 0/1 knapsack problem using dynamic programming?	mcq	\N	\N	2
b411c5f5-22d3-4e83-88dd-b9ffc25ea0f9	d8952437-3b57-4e50-aa0a-58450faabbe7	Consider a hash table with 10 slots, and a hash function that maps each key to one of the slots. If 5 keys are inserted into the hash table, what is the probability that at least one slot contains more than one key?	nat	0.672	\N	2
7971e9c2-77e3-4d81-b02c-657b738d89e8	d8952437-3b57-4e50-aa0a-58450faabbe7	Which of the following algorithms is used to find the shortest path in a graph with negative weight edges?	mcq	\N	\N	1
4aef93e8-1694-4d03-a077-589fab9c0aea	d8952437-3b57-4e50-aa0a-58450faabbe7	Consider a binary search tree with the following properties: all leaves are at the same level, and all internal nodes have two children. If the tree has 7 nodes, what is the height of the tree?	nat	2	\N	1
4757ab38-c85d-4e0a-b931-b9341d56b42c	d8952437-3b57-4e50-aa0a-58450faabbe7	Which of the following statements are true about the merge sort algorithm?	msq	\N	\N	2
11348fba-281c-47e1-8cdf-8f7b5b8daa07	d8952437-3b57-4e50-aa0a-58450faabbe7	Consider a queue with 5 elements. If two elements are dequeued and then three elements are enqueued, what is the total number of elements in the queue?	nat	6	\N	1
8e77a418-d3da-432c-a63b-06f879f73fd9	d8952437-3b57-4e50-aa0a-58450faabbe7	What is the time complexity of the algorithm that finds the closest pair of points in a set of n points in a 2D plane?	mcq	\N	\N	2
5ec6fb4c-1b6b-4196-8034-efd763a388df	d8952437-3b57-4e50-aa0a-58450faabbe7	Consider a graph with 10 vertices and 15 edges. If the graph is represented using an adjacency list, what is the total number of nodes in the adjacency list?	nat	25	\N	2
8199c5d6-ba28-4345-8958-ff6284631966	d8952437-3b57-4e50-aa0a-58450faabbe7	Which of the following algorithms is used to find the maximum flow in a flow network?	mcq	\N	\N	1
321bf669-87fa-4948-902c-8239e2976ce1	d8952437-3b57-4e50-aa0a-58450faabbe7	Consider a stack with 5 elements. If two elements are popped and then three elements are pushed, what is the total number of elements in the stack?	nat	6	\N	1
6a9ca104-de2a-4374-ad79-73d7d5bb8e67	cd85a117-60c2-4b20-97da-f54a9ade7349	A graph has 8 vertices and 12 edges. The maximum number of edges in a spanning tree of this graph is	nat	7	\N	1
0f17501c-a773-49b7-a1d8-92aa4f5f5cb2	cd85a117-60c2-4b20-97da-f54a9ade7349	Consider the following recurrence relation: T(n) = 2T(n/2) + n. What is the value of T(64)?	nat	1344	\N	2
f867a149-8d3f-4796-a039-45361d526c5c	cd85a117-60c2-4b20-97da-f54a9ade7349	Which of the following sorting algorithms has the best average-case time complexity?	mcq	\N	\N	1
c487205c-0949-4dda-aebc-c2439701b692	cd85a117-60c2-4b20-97da-f54a9ade7349	A queue is implemented using two stacks. The time complexity of the enqueue operation is	mcq	\N	\N	1
7bda0e99-7548-4836-a60c-fc6cd7baf439	cd85a117-60c2-4b20-97da-f54a9ade7349	Consider a hash table with 10 slots. The hash function used is h(k) = k mod 10. Which of the following keys will collide?	msq	\N	\N	2
24d44832-acc6-4f5b-b18b-807c1626b243	cd85a117-60c2-4b20-97da-f54a9ade7349	The time complexity of the closest pair algorithm is	mcq	\N	\N	2
71d74946-eb71-4d78-897f-b66fdf968a12	cd85a117-60c2-4b20-97da-f54a9ade7349	A binary search tree has the following property: for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The height of the tree is	nat	3	\N	1
95a185ab-2b30-45b6-8b49-1b24deb1c070	cd85a117-60c2-4b20-97da-f54a9ade7349	Consider the following algorithm: for i = 1 to n, for j = 1 to i, print(i). The time complexity of this algorithm is	mcq	\N	\N	1
e197e100-910f-46fc-b399-a39b6900256c	cd85a117-60c2-4b20-97da-f54a9ade7349	A minimum spanning tree of a graph has 5 edges. The number of vertices in the graph is	nat	6	\N	1
8f353142-c086-4786-bea6-00ce7fca6c76	cd85a117-60c2-4b20-97da-f54a9ade7349	Consider the following recurrence relation: T(n) = T(n/2) + 1. The value of T(256) is	nat	8	\N	2
9e95fa6b-fee1-4b0f-9d29-0211f91ce6ba	97307c87-09f5-4ea9-b998-f4df904b8e0c	What is the time complexity of the following algorithm: for i in range(n): for j in range(i): print(i*j)	mcq	\N	\N	2
9a102505-4e4f-4374-b013-c1277348a290	97307c87-09f5-4ea9-b998-f4df904b8e0c	Suppose we have a stack of integers and we want to find the maximum element in the stack. We can use a temporary stack to solve this problem. What is the time complexity of this approach?	msq	\N	\N	1
1f123ce1-b29c-401c-b28f-4161eb5cb768	97307c87-09f5-4ea9-b998-f4df904b8e0c	A binary search tree with n nodes has a height of 5. What is the maximum number of nodes that can be in the tree?	nat	31	\N	2
40e4b58d-bd82-4108-babd-f8f2798ba658	97307c87-09f5-4ea9-b998-f4df904b8e0c	Which of the following data structures can be used to implement recursion?	mcq	\N	\N	1
f22ab01c-fa61-4bbe-86a8-976c990f4fbd	97307c87-09f5-4ea9-b998-f4df904b8e0c	Suppose we have a graph with n vertices and m edges. We want to find the shortest path between two vertices using Dijkstra's algorithm. What is the time complexity of this approach?	msq	\N	\N	2
19f7edc2-776f-4b45-a69d-6fcb701009ca	97307c87-09f5-4ea9-b998-f4df904b8e0c	A hash table with 10 slots is used to store 15 elements. What is the load factor of the hash table?	nat	1.5	\N	1
d0009aaf-1f3f-44d7-9b34-2fa8698b9be5	97307c87-09f5-4ea9-b998-f4df904b8e0c	Which of the following sorting algorithms has a time complexity of O(n log n) in the worst case?	mcq	\N	\N	2
be1eaa89-3a7b-4bd7-a490-35805bc40342	97307c87-09f5-4ea9-b998-f4df904b8e0c	Suppose we have a set of integers and we want to find the maximum subset sum. Which of the following algorithms can be used to solve this problem?	msq	\N	\N	1
80abb5b0-c261-413d-bec7-8a199b83f8d6	97307c87-09f5-4ea9-b998-f4df904b8e0c	A queue with 10 elements is used to implement a breadth-first search algorithm. What is the maximum number of elements that can be in the queue at any given time?	nat	10	\N	2
ea123688-dabc-4d49-89a4-5d2bd84502ab	97307c87-09f5-4ea9-b998-f4df904b8e0c	Which of the following data structures can be used to implement a cache?	mcq	\N	\N	1
c256b0f8-1330-45c8-b2d2-74d4e2d00d5b	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Consider the language L = {0^n 1^n | n ≥ 0}. Which of the following statements is TRUE?	mcq	\N	\N	1
53b9f793-3904-4a16-a791-62d7d777f07c	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	If a Turing machine M has 5 states and 3 symbols in its tape alphabet, what is the minimum number of states required in the tape of its equivalent universal Turing machine?	nat	10	\N	2
7fb14f3a-9745-4697-a910-11195f286576	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Which of the following statements are TRUE about the language L = {a^m b^n | m ≠ n}?	msq	\N	\N	2
cc41fd8e-1bb8-4fb7-9744-6ccee2be156a	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Consider a pushdown automaton P with 3 states and 2 stack symbols. If P recognizes the language L = {0^n 1^n | n ≥ 0}, what is the minimum number of stack symbols required?	nat	2	\N	1
10a5ac9f-fef2-4460-8558-0c4c38e3dae8	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Which of the following languages are recognized by a deterministic finite automaton?	msq	\N	\N	2
75d0839c-3935-4777-b82d-d67eff0d9303	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Consider the language L = {a^m b^n | m ≥ n}. Which of the following statements is TRUE?	mcq	\N	\N	1
22712d16-bac2-419b-ac32-e70d6d7cfffe	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	If a language L is recognized by a nondeterministic Turing machine in O(n^2) time, what is the minimum time complexity required by a deterministic Turing machine to recognize L?	nat	4	\N	2
57b10240-63b6-49ad-be2f-50fc87002c24	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Which of the following statements are TRUE about the language L = {a^n b^n | n ≥ 0}?	msq	\N	\N	1
1992b693-27fb-4a36-b6d8-5bb5b7e0840a	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Consider a language L recognized by a pushdown automaton P. If P has 4 states and 3 stack symbols, what is the minimum number of states required in the equivalent Turing machine?	nat	12	\N	2
67e1c4c7-c1a7-4bf6-8300-481d9512b9e8	d322d3ce-45d7-4f79-bed9-7e85d67ed4f0	Which of the following languages are recognized by a nondeterministic finite automaton?	mcq	\N	\N	1
412e770d-f53e-4a09-8ec0-cb5e25dbd754	6b680e6e-88ba-4429-9d35-cb793ee99891	Consider a compiler that uses a top-down parser with a lookahead of 1 token. If the parser encounters a syntax error, what is the minimum number of tokens it needs to read to recover from the error?	nat	2	\N	1
2fe57dc2-6639-4a14-8dbf-a3e0d2089dc5	6b680e6e-88ba-4429-9d35-cb793ee99891	Which of the following is a characteristic of a bottom-up parser?	mcq	\N	\N	1
2aa99553-a452-4296-9776-0a43ee721606	6b680e6e-88ba-4429-9d35-cb793ee99891	A compiler uses a hash table to store the symbols in the symbol table. If the hash function used is h(k) = k mod 10, and the compiler encounters a symbol with a hash value of 3, what is the index at which the symbol will be stored in the hash table?	nat	3	\N	2
619db5d7-7552-4a96-aad8-ae9b95eaf666	6b680e6e-88ba-4429-9d35-cb793ee99891	Which of the following are advantages of using a recursive descent parser?	msq	\N	\N	2
03c26caf-7bc4-4e11-aa5f-15489bf4cd39	6b680e6e-88ba-4429-9d35-cb793ee99891	A compiler uses a lexical analyzer to tokenize the input source code. If the lexical analyzer encounters a keyword with a length of 5 characters, what is the minimum number of states required in the finite state machine to recognize the keyword?	nat	6	\N	1
10e5babe-90de-4e8d-bc1d-6f88d9ed0fe2	6b680e6e-88ba-4429-9d35-cb793ee99891	Which of the following is a type of intermediate code used in compilers?	mcq	\N	\N	1
ab6559af-52e7-42e6-bb9d-261ba75b5487	6b680e6e-88ba-4429-9d35-cb793ee99891	A compiler uses a register allocator to allocate registers to variables. If the compiler has 10 available registers and 15 variables to allocate, what is the minimum number of spills required to allocate all variables?	nat	5	\N	2
38dcb3ea-1848-49b4-9f23-7138e44c28ab	6b680e6e-88ba-4429-9d35-cb793ee99891	Which of the following are techniques used in compiler optimization?	msq	\N	\N	2
03dc5b27-a039-4f72-b515-60254a780751	6b680e6e-88ba-4429-9d35-cb793ee99891	A compiler uses a parser to parse the input source code. If the parser encounters a syntax error, what is the minimum number of tokens it needs to read to recover from the error, assuming a lookahead of 2 tokens?	nat	3	\N	1
25470246-ebaa-4bc5-a248-cbad43071036	6b680e6e-88ba-4429-9d35-cb793ee99891	Which of the following is a characteristic of a just-in-time compiler?	mcq	\N	\N	2
6f39571a-44e8-4995-8199-f328dc53b4a1	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	Consider a compiler that uses a top-down parsing approach. If the grammar for the source language is LL(1), what is the maximum number of tokens that the parser needs to look ahead to parse the input string?	mcq	\N	\N	1
409201b6-dfde-4822-bfec-20bb06777775	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	A lexical analyzer uses a finite state machine to recognize tokens in the input stream. If the finite state machine has 10 states and the input stream has 20 characters, what is the maximum number of states that the finite state machine can be in after processing the entire input stream?	nat	10	\N	2
b25d533f-e753-4b29-a4fd-fd3c1c796010	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	Consider a compiler that uses a bottom-up parsing approach. If the grammar for the source language is LR(1), what are the possible parsing table entries for a given production rule?	msq	\N	\N	1
a0d78745-969e-4f10-b4e9-e877441a9af0	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	A syntax-directed translation scheme uses a set of translation rules to generate intermediate code. If the translation rules are based on a given grammar, what is the maximum number of translation rules that can be generated for a given non-terminal symbol?	nat	5	\N	1
4b9e758f-f879-489c-bb46-bb0ef09a99c8	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	Consider a compiler that uses a recursive descent parser to parse the input stream. If the parser has 5 non-terminal symbols and 10 production rules, what is the maximum number of function calls that the parser can make to parse the input stream?	mcq	\N	\N	2
d241619a-4570-453d-9a10-953bc61765c2	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	A code optimizer uses a set of optimization techniques to improve the performance of the generated code. If the optimizer uses a peephole optimization technique, what is the maximum number of instructions that the optimizer can examine to perform the optimization?	nat	3	\N	1
8c6e5646-726b-45e9-a7f5-0ff8093aa552	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	Consider a compiler that uses a register allocation algorithm to allocate registers to variables. If the algorithm uses a graph coloring approach, what are the possible allocation strategies for a given variable?	msq	\N	\N	2
00c3d268-9ee8-4ed0-ba5f-7ca348d5ca0e	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	A compiler uses a symbol table to manage the symbols in the source program. If the symbol table has 100 entries and the compiler uses a hash table to implement the symbol table, what is the average time complexity of a symbol table lookup operation?	nat	1	\N	1
5f04f6ee-6902-471d-a17f-3521f28a0f59	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	Consider a compiler that uses a dead code elimination algorithm to eliminate dead code from the generated code. If the algorithm uses a control flow graph to represent the program, what are the possible types of dead code that the algorithm can eliminate?	msq	\N	\N	2
3c2c0705-7f3b-4e01-8eed-b7007495895c	d01b497b-5f8c-4880-8e6d-19dc66fd82bd	A compiler uses a instruction selection algorithm to select the instructions for the generated code. If the algorithm uses a tree pattern matching approach, what is the maximum number of instruction patterns that the algorithm can match for a given instruction?	mcq	\N	\N	1
e3d6d286-e685-47f1-b6f7-6506d79035a0	a19a588f-7078-4453-ae2d-665e731164cc	Consider a compiler that uses a top-down parser with a lookahead of 1 token. What is the maximum number of tokens that can be parsed in a single left-derivation?	nat	10	\N	2
fac1e92e-f735-45a5-aee6-9c253b0c5de2	a19a588f-7078-4453-ae2d-665e731164cc	Which of the following is NOT a characteristic of a context-free grammar?	mcq	\N	\N	1
b54335a2-771f-481e-959d-e70c0027699a	a19a588f-7078-4453-ae2d-665e731164cc	A lexical analyzer uses a finite state machine to recognize tokens. If the finite state machine has 10 states and the input string has 20 characters, what is the maximum number of transitions that can occur?	nat	30	\N	2
8b4f7e94-30b9-46fc-a427-b6b0f4e49702	a19a588f-7078-4453-ae2d-665e731164cc	Which of the following parsing techniques is the most efficient for parsing a context-free grammar?	mcq	\N	\N	1
22c9a168-0953-4374-beaa-442aa46a5976	a19a588f-7078-4453-ae2d-665e731164cc	Consider a compiler that uses a symbol table to keep track of variable declarations. If the symbol table has 100 entries and each entry requires 10 bytes of memory, what is the total amount of memory required to store the symbol table?	nat	1000	\N	1
990476ab-94b6-4810-b75e-94ebb0acdef4	a19a588f-7078-4453-ae2d-665e731164cc	Which of the following are advantages of using a bottom-up parser?	msq	\N	\N	2
c88d2dd9-8d18-4847-8bb6-5d33246ed2a4	a19a588f-7078-4453-ae2d-665e731164cc	A compiler uses a hash table to store the symbol table. If the hash table has 1000 buckets and the load factor is 0.5, what is the maximum number of symbols that can be stored in the hash table?	nat	500	\N	2
0fdcbe36-255c-428f-a017-b9ad944c89f7	a19a588f-7078-4453-ae2d-665e731164cc	Which of the following is a characteristic of a lexical analyzer?	mcq	\N	\N	1
f893fa34-00a5-446f-9e04-89db0cd1511e	a19a588f-7078-4453-ae2d-665e731164cc	Consider a compiler that uses a three-address code as its intermediate representation. If the three-address code has 100 instructions and each instruction requires 10 bytes of memory, what is the total amount of memory required to store the three-address code?	nat	1000	\N	2
edefd79b-90f6-4e62-bc9b-b7f88b550de4	a19a588f-7078-4453-ae2d-665e731164cc	Which of the following are phases of a compiler?	msq	\N	\N	2
\.


--
-- Data for Name: options; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.options (id, question_id, option_text, is_correct) FROM stdin;
95fb0dca-6045-4496-aeac-8b32b62e1a2b	d2fdde2e-258a-42e0-aed4-42052202d787	6	f
69bbe2dd-95e5-4259-8ff7-e809d3131b29	d2fdde2e-258a-42e0-aed4-42052202d787	7	f
d73d1413-1388-4f0c-892f-f1b4e6a0be92	d2fdde2e-258a-42e0-aed4-42052202d787	8	t
abe092f4-d8a7-48da-bee7-49ade012a67b	d2fdde2e-258a-42e0-aed4-42052202d787	9	f
30995e25-bd49-4771-acf2-62a27dced9b6	71c52cf4-2fe9-4742-89ad-64945f566170	O(n)	f
feb96f82-1889-420d-a40b-e6ee71a63022	71c52cf4-2fe9-4742-89ad-64945f566170	O(n log n)	f
fd13afaf-d442-4d9e-b70e-6a05fff78b0d	71c52cf4-2fe9-4742-89ad-64945f566170	O(n^2)	t
e52f4a31-2ce3-4f44-8406-7fbc7ccb0c13	71c52cf4-2fe9-4742-89ad-64945f566170	O(n^3)	f
e090e1ae-053a-47db-ae56-19befdb45b74	53b0fb59-9a9d-4e8a-8ac6-e95eab348a07	Merge sort	t
7ceb5d08-fdfa-4823-afee-c53d342b28d8	53b0fb59-9a9d-4e8a-8ac6-e95eab348a07	Quick sort	f
ee78a7a0-925c-4766-b43d-8ecfa0dfac97	53b0fb59-9a9d-4e8a-8ac6-e95eab348a07	Heap sort	f
ca221898-9c70-49bd-b89a-3fc5f8efba86	53b0fb59-9a9d-4e8a-8ac6-e95eab348a07	Bubble sort	f
6fb37111-6e5e-4f2a-9845-60c74ce3a40f	dc8d66f0-f40e-49bb-8d79-3c49b12d9669	Stack	t
2898b9ef-c988-40de-aabd-8d924c427b27	dc8d66f0-f40e-49bb-8d79-3c49b12d9669	Queue	f
2036615b-4d94-4381-a968-004ae0a457b3	dc8d66f0-f40e-49bb-8d79-3c49b12d9669	Tree	f
310a854e-0263-4b64-8451-58b1b0cd6365	dc8d66f0-f40e-49bb-8d79-3c49b12d9669	Graph	f
d8b99ffd-cd89-42b8-8817-c332eb755efc	36e3ca52-f8cc-46b8-bc8d-f875f99ff428	O(n)	f
e15f808c-a0fd-42ee-9d30-86fb95011b07	36e3ca52-f8cc-46b8-bc8d-f875f99ff428	O(n log n)	f
b74a3d6d-0006-4f97-a9d6-780d8daae0c2	36e3ca52-f8cc-46b8-bc8d-f875f99ff428	O(n^2)	t
6335bb77-f64d-4a1d-948a-c964940ddf7d	36e3ca52-f8cc-46b8-bc8d-f875f99ff428	O(n^3)	f
4281c3f6-9077-4bc4-800d-b7eabef1dd67	34d82888-578d-48ec-8155-7ab223d2c365	Dijkstra's algorithm	t
a5bcace8-cac9-4354-b8e7-78f304ecf206	34d82888-578d-48ec-8155-7ab223d2c365	Bellman-Ford algorithm	t
171928a0-04e4-428f-b49c-a5d69b68d351	34d82888-578d-48ec-8155-7ab223d2c365	Floyd-Warshall algorithm	t
934bc22e-ce44-498d-ab5b-35aa5d609520	34d82888-578d-48ec-8155-7ab223d2c365	Topological sort	f
2c708fff-6a3d-4abe-a276-5b16121a3e4e	3932836f-fd4e-469e-ba1a-79904aad2d7f	O(n log n)	t
633cf597-9731-4a48-aff7-5fddd0dec3ee	3932836f-fd4e-469e-ba1a-79904aad2d7f	O(n^2)	f
60efc255-40ba-43f0-bf5a-8153c44cf9eb	3932836f-fd4e-469e-ba1a-79904aad2d7f	O(n log n log n)	f
a6944a63-a38f-481d-92a9-ab54d2b0c39c	3932836f-fd4e-469e-ba1a-79904aad2d7f	O(n^3)	f
df48d0ee-a91f-4c7c-9b73-73ebffd138aa	f55db56b-7033-407b-a03d-1b74697b3097	O(n)	f
12b01b88-468e-45a1-8982-b9ef5dbc62d3	f55db56b-7033-407b-a03d-1b74697b3097	O(n log n)	f
1167a72e-f265-4ce2-b24d-f45f20c383be	f55db56b-7033-407b-a03d-1b74697b3097	O(n^2)	t
d79f40ff-5493-44a6-8d40-b6d1191b486e	f55db56b-7033-407b-a03d-1b74697b3097	O(n^3)	f
c25e6980-10c5-4478-a5ce-8c8b13be9a75	28dc92ad-6964-411e-b89d-ca1e075c5edb	Insertion	t
4f6ddacb-3e8d-4774-b3bf-d4f20860f5ff	28dc92ad-6964-411e-b89d-ca1e075c5edb	Deletion	t
60fce6a3-2292-4d6d-9f88-63cb43c22fb9	28dc92ad-6964-411e-b89d-ca1e075c5edb	Search	t
e383a165-9c23-4db8-afe7-595eb7a731a6	28dc92ad-6964-411e-b89d-ca1e075c5edb	All of the above	f
3927895f-9b7d-4ab7-94ef-58b88d0c7a81	a75fb4da-4b2b-4540-b7d2-d13d0a82aa85	20 seconds	f
2292d04c-4193-4fe8-a13c-2eb13a693b1c	a75fb4da-4b2b-4540-b7d2-d13d0a82aa85	40 seconds	t
bdb3f811-7656-497f-9dc6-b872859c57f5	a75fb4da-4b2b-4540-b7d2-d13d0a82aa85	60 seconds	f
0cc95b05-8560-4cb2-b8dd-3836356a813e	a75fb4da-4b2b-4540-b7d2-d13d0a82aa85	80 seconds	f
c6cbbb7b-6d1d-4fbb-84e6-2403a1ca105e	4df0415e-cf5d-4d1f-89c5-aa553c051875	O(n)	f
706e4bb1-6731-4000-84d0-0e58465d7377	4df0415e-cf5d-4d1f-89c5-aa553c051875	O(n log n)	t
679401bc-c0f6-4e5b-8873-710a4713698d	4df0415e-cf5d-4d1f-89c5-aa553c051875	O(n^2)	f
ce5f182f-fe24-4796-baf9-a9a39eb12163	4df0415e-cf5d-4d1f-89c5-aa553c051875	O(2^n)	f
56f10fea-7a6d-4e46-bb64-9d762e2e83a1	abb6da13-f02e-49e0-baab-ad0236cb6641	Enqueue	t
136df392-7a39-4186-a592-8afa5b80ee2b	abb6da13-f02e-49e0-baab-ad0236cb6641	Dequeue	t
21af166f-f5d3-42c3-b8a7-02301e10288e	abb6da13-f02e-49e0-baab-ad0236cb6641	Peek	t
51e341ff-1195-45cb-95a6-9c36e67862ee	abb6da13-f02e-49e0-baab-ad0236cb6641	All of the above	f
cca61864-26c3-4241-9904-d0973625c014	a1af9a53-2049-4001-a4df-74efdd5bc1c8	Dijkstra's algorithm	f
df933973-cf10-4308-bf97-3d28fcf516be	a1af9a53-2049-4001-a4df-74efdd5bc1c8	Bellman-Ford algorithm	f
41fd7d20-6443-4ffa-a023-75c37a895f48	a1af9a53-2049-4001-a4df-74efdd5bc1c8	Kruskal's algorithm	t
430c8ced-e068-461f-9702-80814fa05579	a1af9a53-2049-4001-a4df-74efdd5bc1c8	Floyd-Warshall algorithm	f
baa2f353-3ce9-451e-80fd-d494e5f8e393	da6c75f1-b80e-4ac2-ab32-04af44be471b	O(n)	f
f6eb9031-eb8f-4584-87b5-b24ad6785897	da6c75f1-b80e-4ac2-ab32-04af44be471b	O(n log n)	f
efbfbf05-c60e-4873-98be-df73293152f3	da6c75f1-b80e-4ac2-ab32-04af44be471b	O(n^2)	t
8f07e503-3249-487d-a746-057db515c38f	da6c75f1-b80e-4ac2-ab32-04af44be471b	O(2^n)	f
e90dc9fb-5135-4420-bf13-6b7f5a080044	2cf38472-2ee8-4d40-aac4-f1004626937f	10, 30	t
ca3c7b20-926e-411f-9def-534786bf2ae0	2cf38472-2ee8-4d40-aac4-f1004626937f	20, 20	f
0fa9a856-ed55-4195-a3e3-6b4cb63a3f75	2cf38472-2ee8-4d40-aac4-f1004626937f	15, 25	f
c9295eaf-b332-472c-8ff2-09ca673573bb	2cf38472-2ee8-4d40-aac4-f1004626937f	25, 15	t
5eb7a512-de15-4039-8319-9280f6b7c6ed	99ad7253-6e5c-4d45-a793-024e1cc5d179	$0.05	t
de32aefa-31b3-4370-b192-1f16ec5d789e	99ad7253-6e5c-4d45-a793-024e1cc5d179	$0.10	f
2896aaef-d823-47e6-b505-7642ec1d2683	99ad7253-6e5c-4d45-a793-024e1cc5d179	$0.15	f
9a1c03c4-7bff-4a68-969e-a4d16917313e	99ad7253-6e5c-4d45-a793-024e1cc5d179	$0.20	f
5cbdbe92-0ef7-48bf-a2ba-7c0f89ffd74f	b7c19f7a-a918-4812-b83d-33b6d5892cae	The probability of drawing a red ball is greater than the probability of drawing a blue ball	t
3cc290e1-aafa-48f7-b68f-182565a00922	b7c19f7a-a918-4812-b83d-33b6d5892cae	The probability of drawing a green ball is less than the probability of drawing a blue ball	t
849e3404-a3c5-4d0a-ae1b-5ac184297a74	b7c19f7a-a918-4812-b83d-33b6d5892cae	The probability of drawing a red ball is less than the probability of drawing a blue ball	f
7be7dd66-dbc2-4616-b9a3-ad2d7683fb3d	b7c19f7a-a918-4812-b83d-33b6d5892cae	The probability of drawing a green ball is greater than the probability of drawing a blue ball	f
3862a34e-0d31-489f-b616-9c60e48e50ff	1bc995ea-0278-4080-a250-2446d6334af0	60%	f
9eb4f054-8fd4-4aca-a8f0-e07a529cae30	1bc995ea-0278-4080-a250-2446d6334af0	70%	t
6c7a7b98-b70b-4601-96d0-b031bafa57e4	1bc995ea-0278-4080-a250-2446d6334af0	80%	f
b30eed10-c879-446c-9e2f-1cfa4d201d04	1bc995ea-0278-4080-a250-2446d6334af0	90%	f
d9bedd27-cd2a-4746-9f6d-f6b52ef77e9b	2c31ae06-e084-4298-921d-469e0d8ec6e8	J1=1, K1=1, J4=1, K4=0	t
5ae2a16a-32d8-47d2-b526-837c86bf15a0	2c31ae06-e084-4298-921d-469e0d8ec6e8	J1=1, K1=0, J4=1, K4=1	f
7970f3d3-a411-420a-a1c2-905a4f909598	2c31ae06-e084-4298-921d-469e0d8ec6e8	J1=0, K1=1, J4=1, K4=0	f
1c987c20-1441-43fc-bb34-bec5fe382d2b	2c31ae06-e084-4298-921d-469e0d8ec6e8	J1=1, K1=1, J4=0, K4=1	t
4ef10aab-2b57-44b4-8e3e-82debf25bf5d	e72e3503-6ad5-434a-ad4f-2a114754f863	6	f
79c8dc6a-d8aa-4ddc-9eb6-ea54d3a067b7	e72e3503-6ad5-434a-ad4f-2a114754f863	8	t
12d70962-4873-4f40-bacc-d22fdaa1b967	e72e3503-6ad5-434a-ad4f-2a114754f863	10	f
60ed7a8c-5fa1-4a0d-ba53-1d552408e3e8	e72e3503-6ad5-434a-ad4f-2a114754f863	12	f
0d9d62c1-617d-4230-a6e9-09063019e247	7307fbc3-b443-4c5f-9a7b-9d7b94e346ae	0	t
d0af4e0d-7b25-4190-a24c-829352f6f878	7307fbc3-b443-4c5f-9a7b-9d7b94e346ae	1	f
dd4ce9c5-ec14-401e-8ba1-40762aac5c9a	7307fbc3-b443-4c5f-9a7b-9d7b94e346ae	A AND B	f
3bf54c21-99d4-498d-9867-49ca43dc2114	7307fbc3-b443-4c5f-9a7b-9d7b94e346ae	A OR B	f
3e92b203-c88b-467c-9978-9cb4701a3fb5	63dedc19-b54f-4736-b99e-c1a3a6831acf	A=0, B=0	f
47bb4be8-9049-4505-a9bd-c2bce202ae58	63dedc19-b54f-4736-b99e-c1a3a6831acf	A=0, B=1	t
84ca88d4-a0fa-49fd-b15c-65216358d786	63dedc19-b54f-4736-b99e-c1a3a6831acf	A=1, B=0	f
3aa66062-db04-4a88-87d2-a1445a946a69	63dedc19-b54f-4736-b99e-c1a3a6831acf	A=1, B=1	t
09754da2-8063-4b03-9cce-b4c688750d1d	8015b04f-b9d4-49fa-b18a-b84a0437eb57	A=0, B=0	f
8f3a143e-c372-405d-b35f-0cc07a7f8c8c	8015b04f-b9d4-49fa-b18a-b84a0437eb57	A=0, B=1	f
fb6ee8f9-2e1f-42fd-b3f0-0c1ae1bc08f4	8015b04f-b9d4-49fa-b18a-b84a0437eb57	A=1, B=0	t
6acca7ca-30f3-4d3b-aef9-ac0d5f4c71f0	8015b04f-b9d4-49fa-b18a-b84a0437eb57	A=1, B=1	f
d37389ac-85dd-4d6f-ba38-4beea4e51a8d	e1cc1467-6542-41b4-8474-a1eeaafe25d9	Merge Sort	t
f847e435-d899-4e28-9974-ed87b2f79de4	e1cc1467-6542-41b4-8474-a1eeaafe25d9	Quick Sort	f
0288cd75-a3f2-4ecf-9587-1fbc89056b2e	e1cc1467-6542-41b4-8474-a1eeaafe25d9	Heap Sort	f
559fff38-8cee-465b-9ee8-6e6e216b4a43	e1cc1467-6542-41b4-8474-a1eeaafe25d9	Insertion Sort	f
38194e26-621f-4182-b3a8-4b81c0517ff0	27a286dd-72b1-4bba-9d15-e126bc8d59f2	It uses a priority queue to select the next vertex	t
42888d13-cf57-4927-ab2e-a42771720ca5	27a286dd-72b1-4bba-9d15-e126bc8d59f2	It can handle negative weight edges	f
09cdb700-28ea-4a30-875e-0f4bc92533bb	27a286dd-72b1-4bba-9d15-e126bc8d59f2	It is used for finding the shortest path in a graph	t
20b28e9a-df9e-4173-9f3d-633306e41f68	27a286dd-72b1-4bba-9d15-e126bc8d59f2	It has a time complexity of O(n^2)	f
9d071194-6418-432b-9db2-ae8b85abca4d	be49b3ea-1b99-4102-94fb-51a240ad9804	Ford-Fulkerson algorithm	t
f8932321-4d41-4fd9-a083-2d53f489e2f3	be49b3ea-1b99-4102-94fb-51a240ad9804	Dijkstra's algorithm	f
404c2b8b-6fab-4224-ad37-5d52b4b65af0	be49b3ea-1b99-4102-94fb-51a240ad9804	Bellman-Ford algorithm	f
80a03d4b-c48b-40c7-9207-92767073b25b	be49b3ea-1b99-4102-94fb-51a240ad9804	Topological Sort	f
0b547038-c176-4785-ad89-db72948a12f1	5e6c6aa8-e6ce-46a6-a12d-2b8fe4e0791a	It uses a stack to traverse the graph	t
ec23a498-492e-431e-8ab5-265d43b06b55	5e6c6aa8-e6ce-46a6-a12d-2b8fe4e0791a	It can be used to find the connected components of a graph	t
50b379c7-8404-4b1b-943f-5a1237aa82e9	5e6c6aa8-e6ce-46a6-a12d-2b8fe4e0791a	It has a time complexity of O(n^2)	f
0ff59049-641f-40e7-801e-a7d51fc004d4	5e6c6aa8-e6ce-46a6-a12d-2b8fe4e0791a	It can handle negative weight edges	f
07d53b2b-60eb-4e6d-9ee9-30aadb962bea	3ff051d6-1a64-476f-9bb9-dbf60cb43ea0	Bubble Sort	f
cd5a551e-34b9-448e-b450-b7e01e197483	3ff051d6-1a64-476f-9bb9-dbf60cb43ea0	Selection Sort	t
15f678ac-4fea-4578-872a-499dbcca329f	3ff051d6-1a64-476f-9bb9-dbf60cb43ea0	Insertion Sort	f
30a25088-1e34-4a70-bc78-9e9e85b0c292	3ff051d6-1a64-476f-9bb9-dbf60cb43ea0	Merge Sort	f
10a78701-846e-49e7-b313-18ce358fe399	acf5cabb-37c1-44ee-9720-14230825f1f6	xy' + y = 0	f
c57f25e4-6405-40bb-85dc-ec04785ec8d0	acf5cabb-37c1-44ee-9720-14230825f1f6	xy' - y = 0	f
aebb3d2e-94e0-48f6-a5f7-9d504ea40c59	acf5cabb-37c1-44ee-9720-14230825f1f6	y' = (y - B)/x	t
27b50975-00ba-4d93-a6ce-3ff22756c1f1	acf5cabb-37c1-44ee-9720-14230825f1f6	y' = (B - y)/x	f
d2081a14-0d70-4eb8-81ca-242df6b47128	4257b4b8-6ada-4355-82c3-37f7361742fc	an even function	f
43dc7cd4-7600-4eec-b4f3-5ba30c10fd0e	4257b4b8-6ada-4355-82c3-37f7361742fc	an odd function	f
5bfa9410-3a46-4fe8-8526-e3840f9cc5c5	4257b4b8-6ada-4355-82c3-37f7361742fc	a periodic function	f
02e851bc-193a-4ba4-8073-496ee56debc0	4257b4b8-6ada-4355-82c3-37f7361742fc	a monotonic function	t
431d0471-844a-4873-a2f8-14fade373d45	9746ea91-eb00-410a-b37b-2286113bdbef	a unique solution	t
386bc6b5-9999-41c7-86ff-a6979a9b23c8	9746ea91-eb00-410a-b37b-2286113bdbef	no solution	f
ce2dc955-f3eb-4012-b097-fa857c451bf0	9746ea91-eb00-410a-b37b-2286113bdbef	infinitely many solutions	f
e1f04dd5-1414-4ed5-bbf8-e25097a1327d	9746ea91-eb00-410a-b37b-2286113bdbef	two distinct solutions	f
74a7f6bc-7cf6-4183-9b36-96f980de950a	542f2dc1-93ef-4256-97af-229ba5859678	π/2 - (4/π) * ∑[(2n-1)^(-2) * cos((2n-1)x)]	t
699dd46f-b735-4492-b953-c85e3f0cafa7	542f2dc1-93ef-4256-97af-229ba5859678	π/2 - (4/π) * ∑[(2n-1)^(-2) * sin((2n-1)x)]	f
d60f49e7-eca0-4bc3-82f6-127847a64cea	542f2dc1-93ef-4256-97af-229ba5859678	π/2 + (4/π) * ∑[(2n-1)^(-2) * cos((2n-1)x)]	f
25b02d40-1845-4cd5-a070-487a7737c3ec	542f2dc1-93ef-4256-97af-229ba5859678	π/2 + (4/π) * ∑[(2n-1)^(-2) * sin((2n-1)x)]	f
2bb212fe-0798-4950-acec-4a890f86ebd0	b956e9c1-1e64-469b-8f54-d8a4ccb39ff8	one real root and two complex roots	f
cf82647f-3d63-45fc-a097-7fa58fe12965	b956e9c1-1e64-469b-8f54-d8a4ccb39ff8	two real roots and one complex root	f
b48c2eb4-3224-4c74-9cb0-e7f2bb6a051f	b956e9c1-1e64-469b-8f54-d8a4ccb39ff8	three real roots	t
28a1e916-af28-4150-8112-6e25761109ca	b956e9c1-1e64-469b-8f54-d8a4ccb39ff8	three complex roots	f
84409f7b-0762-4f10-8004-9daccea1f8c5	cc66ff75-46e3-4e3e-b01f-13bfe043d865	z = 2	t
b3265e9c-3bf4-49a5-a3c5-89fdcb39fe7e	cc66ff75-46e3-4e3e-b01f-13bfe043d865	z = -2	t
dd93b257-be91-4b0d-b292-5237753ac899	cc66ff75-46e3-4e3e-b01f-13bfe043d865	z = 1	f
5b085897-f8f7-4622-a636-bf2d291a59fc	cc66ff75-46e3-4e3e-b01f-13bfe043d865	z = -1	f
0c95ded4-fc95-4529-b9bf-038de8e7be2e	50acb980-6d53-437a-9591-e55fab88c209	O(nW)	t
21dc1942-c415-41c1-9b35-d5a28ee5e1b3	50acb980-6d53-437a-9591-e55fab88c209	O(2^n)	f
7d56d40f-7f50-476e-aab9-6956ab8e8337	50acb980-6d53-437a-9591-e55fab88c209	O(n^2W)	f
78d7b8f7-a803-45a4-ad28-003eb90a0da5	50acb980-6d53-437a-9591-e55fab88c209	O(nW^2)	f
812185fa-5629-485e-b805-1b95b9a1c993	7971e9c2-77e3-4d81-b02c-657b738d89e8	Dijkstra's algorithm	f
c23d93ab-0671-448a-93db-301379bea54a	7971e9c2-77e3-4d81-b02c-657b738d89e8	Bellman-Ford algorithm	t
67f64fcd-0f6a-4745-b7a2-fed07b9cf1da	7971e9c2-77e3-4d81-b02c-657b738d89e8	Floyd-Warshall algorithm	f
de60fc93-bb76-4e5f-9e1c-de3eac449ea5	7971e9c2-77e3-4d81-b02c-657b738d89e8	Topological sorting	f
7a527e63-47e1-4571-bf28-8f8d5b3649e1	4757ab38-c85d-4e0a-b931-b9341d56b42c	It is an in-place sorting algorithm	f
0634ecb2-bf88-410d-b037-015666841653	4757ab38-c85d-4e0a-b931-b9341d56b42c	It has a time complexity of O(n log n)	t
0d0ff93c-4c82-4171-8747-914f5cac8e40	4757ab38-c85d-4e0a-b931-b9341d56b42c	It is a stable sorting algorithm	t
215364ba-6ac3-4149-a863-1bb16ecd6949	4757ab38-c85d-4e0a-b931-b9341d56b42c	It is a recursive sorting algorithm	t
fd53bd0e-dbc7-4e0d-831d-45be3b48b26d	8e77a418-d3da-432c-a63b-06f879f73fd9	O(n log n)	t
e20600f8-22d1-4b54-b8e6-9e1376600546	8e77a418-d3da-432c-a63b-06f879f73fd9	O(n^2)	f
8615e63e-b3c7-45f9-83da-6e2348745482	8e77a418-d3da-432c-a63b-06f879f73fd9	O(n^2 log n)	f
e974ff49-e8a3-4704-8821-6df8b28ef361	8e77a418-d3da-432c-a63b-06f879f73fd9	O(n log^2 n)	f
ea333ec1-0f6c-4df5-a9a4-203390efa74a	8199c5d6-ba28-4345-8958-ff6284631966	Ford-Fulkerson algorithm	t
f6e59715-aa0b-4e7b-ab4e-f4e471522a98	8199c5d6-ba28-4345-8958-ff6284631966	Dijkstra's algorithm	f
b957877f-0303-455a-bd24-85f83f872e1b	8199c5d6-ba28-4345-8958-ff6284631966	Bellman-Ford algorithm	f
5490ebae-6cc9-4540-adb2-6a62e8f98e48	8199c5d6-ba28-4345-8958-ff6284631966	Topological sorting	f
c400199e-9a47-4aa5-826d-dae1328d9e15	f867a149-8d3f-4796-a039-45361d526c5c	Bubble sort	f
5a284ab0-c9aa-4a1c-aef2-8c359a0c53d8	f867a149-8d3f-4796-a039-45361d526c5c	Selection sort	f
5a3f8805-fd3e-4c5f-b357-2fe038799ab6	f867a149-8d3f-4796-a039-45361d526c5c	Merge sort	t
2fb4e8da-772e-4ca7-8a40-b32c2abfbd1a	f867a149-8d3f-4796-a039-45361d526c5c	Quick sort	f
812dfe09-7c3f-4fc4-8c2e-27817af53f77	c487205c-0949-4dda-aebc-c2439701b692	O(1)	f
3f749a68-6458-41eb-a791-9885cafc4a11	c487205c-0949-4dda-aebc-c2439701b692	O(log n)	f
b813b6d1-727b-4b8c-a301-de513a11b357	c487205c-0949-4dda-aebc-c2439701b692	O(n)	t
3c5c9522-ea4b-4746-8a12-df8b9f7be545	c487205c-0949-4dda-aebc-c2439701b692	O(n log n)	f
ba03e6c1-e7ad-4be5-92b5-90e59afef751	7bda0e99-7548-4836-a60c-fc6cd7baf439	12	t
ce24c97f-524b-4219-b92b-af8c5a011076	7bda0e99-7548-4836-a60c-fc6cd7baf439	22	t
26eebc2b-fe9d-45c5-81cb-55c98cc8a759	7bda0e99-7548-4836-a60c-fc6cd7baf439	32	t
6c2d76fb-9f16-4def-b78b-2fb7658d4c11	7bda0e99-7548-4836-a60c-fc6cd7baf439	42	t
f3a2de21-d5d9-4164-ab61-e345512f9da2	24d44832-acc6-4f5b-b18b-807c1626b243	O(n log n)	t
77d8fb40-58a4-44e2-a9e5-8404fff13a7e	24d44832-acc6-4f5b-b18b-807c1626b243	O(n^2)	f
191dbe3f-b142-4293-81bc-db2f1afa8f88	24d44832-acc6-4f5b-b18b-807c1626b243	O(n^2 log n)	f
e934d309-9556-4f20-b3a9-446ecffbca67	24d44832-acc6-4f5b-b18b-807c1626b243	O(n log^2 n)	f
e5e03c2f-c179-4382-b93b-d6ae0bf71e5f	95a185ab-2b30-45b6-8b49-1b24deb1c070	O(n)	f
8ae1566a-e5e3-41a4-af24-7ea8cdbe7e82	95a185ab-2b30-45b6-8b49-1b24deb1c070	O(n log n)	f
5c5f6da3-1c40-4fcd-aa9b-00d2e0e012c3	95a185ab-2b30-45b6-8b49-1b24deb1c070	O(n^2)	t
23025c9f-c3e3-4834-9b65-9de84e1a27e5	95a185ab-2b30-45b6-8b49-1b24deb1c070	O(n^2 log n)	f
cd56d98a-3cc6-4d0e-984a-6a7364bb21e6	9e95fa6b-fee1-4b0f-9d29-0211f91ce6ba	O(n)	f
e6304330-0ddb-4275-a085-0db99aea5b31	9e95fa6b-fee1-4b0f-9d29-0211f91ce6ba	O(n^2)	t
98ea9fc5-9ae8-4308-9835-b24fd935822c	9e95fa6b-fee1-4b0f-9d29-0211f91ce6ba	O(n^3)	f
37300fe0-86a6-4442-8fae-aa05d0565eb6	9e95fa6b-fee1-4b0f-9d29-0211f91ce6ba	O(2^n)	f
c6fb804f-518b-4e87-b2cb-ce3f336d4cd1	9a102505-4e4f-4374-b013-c1277348a290	O(1)	f
6787214d-1e3d-4283-9e50-9b1ba00baab3	9a102505-4e4f-4374-b013-c1277348a290	O(log n)	f
e7bda627-5077-4561-b5b9-c5b562158132	9a102505-4e4f-4374-b013-c1277348a290	O(n)	t
f16a2d7d-8a28-4835-af50-5599ad71143a	9a102505-4e4f-4374-b013-c1277348a290	O(n^2)	f
0a0c6cd6-ce14-4410-be60-282e71d9b531	40e4b58d-bd82-4108-babd-f8f2798ba658	Stack	t
23f32d49-01b7-42f6-af7b-7aa0f3b5010f	40e4b58d-bd82-4108-babd-f8f2798ba658	Queue	f
1147c1ca-a124-44fb-8e14-679b5842ed8c	40e4b58d-bd82-4108-babd-f8f2798ba658	Tree	f
008e4e36-c636-4d6d-a13c-a800ee172b7f	40e4b58d-bd82-4108-babd-f8f2798ba658	Graph	f
82bc5c9f-f0e3-4b36-9e71-4a419f0a25ab	f22ab01c-fa61-4bbe-86a8-976c990f4fbd	O(n+m)	f
85dd6e67-1171-4c4a-b7aa-8d7b63e9669a	f22ab01c-fa61-4bbe-86a8-976c990f4fbd	O(n^2+m)	t
e1e5cf28-6397-4bdc-8ab8-11dbf5982545	f22ab01c-fa61-4bbe-86a8-976c990f4fbd	O(n^2+m^2)	f
cfd2d664-8f22-469f-956a-4a48bfc794cc	f22ab01c-fa61-4bbe-86a8-976c990f4fbd	O(2^n)	f
3cd5486f-74f2-4897-b6b3-cc992cccc655	d0009aaf-1f3f-44d7-9b34-2fa8698b9be5	Bubble sort	f
ab36f276-c709-4496-ace0-749c494827c3	d0009aaf-1f3f-44d7-9b34-2fa8698b9be5	Selection sort	f
46ed605d-2df9-40e2-8b5f-c8ba5bbc297a	d0009aaf-1f3f-44d7-9b34-2fa8698b9be5	Merge sort	t
2c3c2b84-17b9-47ea-a6cd-505a41a65281	d0009aaf-1f3f-44d7-9b34-2fa8698b9be5	Insertion sort	f
4c4c8447-5464-4f4a-8eb8-4728ae412763	be1eaa89-3a7b-4bd7-a490-35805bc40342	Greedy algorithm	f
184ef120-5ab6-4edd-9b63-d81082e73647	be1eaa89-3a7b-4bd7-a490-35805bc40342	Dynamic programming	t
91d230c1-e1e4-4ca9-9664-363a8f83105b	be1eaa89-3a7b-4bd7-a490-35805bc40342	Backtracking	f
b58a6efa-8ca2-46e5-adfb-a9212b9ab24a	be1eaa89-3a7b-4bd7-a490-35805bc40342	Bit manipulation	f
67de1289-50a0-469f-9548-252b585b2ea1	ea123688-dabc-4d49-89a4-5d2bd84502ab	Stack	f
50bee209-5b73-4ac3-b999-3db510628176	ea123688-dabc-4d49-89a4-5d2bd84502ab	Queue	f
e3b57230-d8c2-4f69-ac51-58ee0e8711a3	ea123688-dabc-4d49-89a4-5d2bd84502ab	Hash table	t
bdde5798-f343-4818-9ed9-5178cbc13fe4	ea123688-dabc-4d49-89a4-5d2bd84502ab	Tree	f
7adc2f92-bae3-4b59-84de-93b6d9365499	c256b0f8-1330-45c8-b2d2-74d4e2d00d5b	L is regular	f
f65ce25b-0e8f-49be-9454-c93bd17a6d60	c256b0f8-1330-45c8-b2d2-74d4e2d00d5b	L is context-free but not regular	t
4890edbd-a407-4e99-808b-8341512756ad	c256b0f8-1330-45c8-b2d2-74d4e2d00d5b	L is not context-free	f
11e384f4-59f9-422d-ab60-759a0aaef9a8	c256b0f8-1330-45c8-b2d2-74d4e2d00d5b	L is recursively enumerable	f
ae7df9f0-18b0-4bbe-a0c5-9aa74b6cbcc1	7fb14f3a-9745-4697-a910-11195f286576	L is context-free	t
3401e9f1-9e9e-4091-8b41-3845b859538e	7fb14f3a-9745-4697-a910-11195f286576	L is regular	f
e9f1808d-9020-4c38-a7fb-786d2202c432	7fb14f3a-9745-4697-a910-11195f286576	L is not context-free	f
f0a3e0e8-2793-429d-a3ff-b47fb298da58	7fb14f3a-9745-4697-a910-11195f286576	L is decidable	t
22d3e453-2ea9-4705-b5bb-9ba364242c3d	10a5ac9f-fef2-4460-8558-0c4c38e3dae8	{a^m b^n | m = n}	t
0384a196-c129-45b4-bfca-3734e6e33297	10a5ac9f-fef2-4460-8558-0c4c38e3dae8	{a^m b^n | m ≠ n}	f
4bf3f7fc-6ea7-45b5-bc3c-bb34f726469b	10a5ac9f-fef2-4460-8558-0c4c38e3dae8	{a^n b^n | n ≥ 0}	t
eae5ff15-2ac4-402e-80b4-e4884bb86589	10a5ac9f-fef2-4460-8558-0c4c38e3dae8	{a^n | n is a prime number}	f
8a5b0e9e-0bed-4c27-95a9-d177858785ae	75d0839c-3935-4777-b82d-d67eff0d9303	L is regular	f
9b0e1ddd-a810-4f6f-ab03-e432815567d2	75d0839c-3935-4777-b82d-d67eff0d9303	L is context-free but not regular	t
fa031342-425c-4f5d-b348-83d1ccb9e03e	75d0839c-3935-4777-b82d-d67eff0d9303	L is not context-free	f
2c180264-8857-4ae2-9475-9c14b2a7f76c	75d0839c-3935-4777-b82d-d67eff0d9303	L is recursively enumerable	f
b5cebe60-5fa2-4199-9cef-77167645fd63	57b10240-63b6-49ad-be2f-50fc87002c24	L is regular	f
90bef2bb-6863-4058-9f9a-120844f811b0	57b10240-63b6-49ad-be2f-50fc87002c24	L is context-free	t
f2b24a90-6d59-4807-b230-c318a1046166	57b10240-63b6-49ad-be2f-50fc87002c24	L is not context-free	f
150b2ffe-158b-4227-8d1d-76d2ff62cba6	57b10240-63b6-49ad-be2f-50fc87002c24	L is decidable	t
fe241538-3ca7-4cdf-9447-daa79e1efc4a	67e1c4c7-c1a7-4bf6-8300-481d9512b9e8	{a^m b^n | m = n}	f
b88fa6b6-394b-4b51-a022-78c909f65b3f	67e1c4c7-c1a7-4bf6-8300-481d9512b9e8	{a^m b^n | m ≠ n}	f
2505ca1f-1469-473c-a881-0fd3b85c595b	67e1c4c7-c1a7-4bf6-8300-481d9512b9e8	{a^n b^n | n ≥ 0}	t
0bbd8624-b3b8-4a06-9f6a-e2141863dfdb	67e1c4c7-c1a7-4bf6-8300-481d9512b9e8	{a^n | n is a prime number}	f
9e3c5806-7a44-45ff-bb54-a0f317c2a08f	2fe57dc2-6639-4a14-8dbf-a3e0d2089dc5	It starts with the overall structure of the program and works its way down to the individual symbols	f
228c30a2-1b59-403a-aa0f-f162fb7c5777	2fe57dc2-6639-4a14-8dbf-a3e0d2089dc5	It starts with the individual symbols and works its way up to the overall structure of the program	t
341d48c4-93fc-4651-b1db-1ade35a56ca6	2fe57dc2-6639-4a14-8dbf-a3e0d2089dc5	It uses a lookahead of 1 token to parse the input	f
92680ecf-aba5-431f-8688-838fd163f4ae	2fe57dc2-6639-4a14-8dbf-a3e0d2089dc5	It uses a lookahead of 2 tokens to parse the input	f
dd741d0c-aec4-4a4a-bcdb-f68fcf3d71a7	619db5d7-7552-4a96-aad8-ae9b95eaf666	It is more efficient than a top-down parser	f
1729189f-79a2-48be-b153-70528101dd26	619db5d7-7552-4a96-aad8-ae9b95eaf666	It is easier to implement than a top-down parser	t
7e9156c1-52a1-4cc5-8bfe-e116c457e17f	619db5d7-7552-4a96-aad8-ae9b95eaf666	It can handle left-recursive grammars	f
41ecc3ec-ee11-4a09-962d-d4446874ad86	619db5d7-7552-4a96-aad8-ae9b95eaf666	It can handle ambiguous grammars	t
4a789797-1609-474d-bb8a-f40b30b75cca	10e5babe-90de-4e8d-bc1d-6f88d9ed0fe2	Three-address code	t
b1b9f8d0-29a6-484e-aa49-1c898ec59288	10e5babe-90de-4e8d-bc1d-6f88d9ed0fe2	Two-address code	f
ba191d19-1f00-4a10-92d0-f9e00bcd78a9	10e5babe-90de-4e8d-bc1d-6f88d9ed0fe2	One-address code	f
857d71a7-74fe-4878-98c4-c636e92b987b	10e5babe-90de-4e8d-bc1d-6f88d9ed0fe2	Zero-address code	f
4fd7f786-00da-44bf-98a1-328951d58e39	38dcb3ea-1848-49b4-9f23-7138e44c28ab	Constant folding	t
6e276c8a-83a4-4dd7-a2f9-cf76ff4191c0	38dcb3ea-1848-49b4-9f23-7138e44c28ab	Constant propagation	t
24f3024b-cf18-49ea-898a-c6276fd87cab	38dcb3ea-1848-49b4-9f23-7138e44c28ab	Dead code elimination	t
1c02350a-b208-409d-8041-1d29c228a8fb	38dcb3ea-1848-49b4-9f23-7138e44c28ab	Register allocation	f
38e5c635-8aef-4e24-8910-8711a7862d62	25470246-ebaa-4bc5-a248-cbad43071036	It compiles the entire program before executing it	f
c0dc2a57-354e-4cd3-b0b0-b426dd060e36	25470246-ebaa-4bc5-a248-cbad43071036	It compiles the program into native machine code	t
1f2f5997-6621-4841-93ba-0f34c5a50d6f	25470246-ebaa-4bc5-a248-cbad43071036	It compiles the program into intermediate code	f
fe9bebd5-923a-4921-918e-7975a95c305c	25470246-ebaa-4bc5-a248-cbad43071036	It compiles the program into bytecode	f
a5ffa765-4700-493f-a922-295dc1aa934b	6f39571a-44e8-4995-8199-f328dc53b4a1	1	t
866c807c-ad2f-475b-9492-95cac547ec7a	6f39571a-44e8-4995-8199-f328dc53b4a1	2	f
487a0233-a580-4b66-9a02-a101625f2f7e	6f39571a-44e8-4995-8199-f328dc53b4a1	3	f
b42a6c3a-e507-44cb-8302-764a2930b4a4	6f39571a-44e8-4995-8199-f328dc53b4a1	4	f
f3791725-4288-4ecc-ac9d-9b2c9cc8015f	b25d533f-e753-4b29-a4fd-fd3c1c796010	Shift	t
58a0e2db-d165-4961-a9da-9a967e5de819	b25d533f-e753-4b29-a4fd-fd3c1c796010	Reduce	t
2e49cb90-3513-46ca-9957-4e6c4e8f64fa	b25d533f-e753-4b29-a4fd-fd3c1c796010	Accept	f
aad97004-6d16-432a-81d9-d41a1aa2deef	b25d533f-e753-4b29-a4fd-fd3c1c796010	Error	f
07533d67-f022-4edb-a34a-81b89f6051cd	4b9e758f-f879-489c-bb46-bb0ef09a99c8	10	f
67c5a6f7-83f8-4e35-bcbe-4ceccb90888b	4b9e758f-f879-489c-bb46-bb0ef09a99c8	15	f
60ea5b44-a442-4069-8ece-f9a76054d2f5	4b9e758f-f879-489c-bb46-bb0ef09a99c8	20	t
20e4e953-620c-4262-9726-726cea43e035	4b9e758f-f879-489c-bb46-bb0ef09a99c8	25	f
eccc1bc6-fabd-4450-a423-4ae7be1b7218	8c6e5646-726b-45e9-a7f5-0ff8093aa552	Spill	t
5ebd2a85-9bbe-4472-8e71-2aabd2f52b26	8c6e5646-726b-45e9-a7f5-0ff8093aa552	Split	f
04132d9f-d662-42da-ba76-1372e6c0af58	8c6e5646-726b-45e9-a7f5-0ff8093aa552	Coalesce	t
3747ca49-73b8-49ae-9a6d-cccefb16feea	8c6e5646-726b-45e9-a7f5-0ff8093aa552	Combine	f
9ed421ab-bf85-481a-88c7-d24dea97f561	5f04f6ee-6902-471d-a17f-3521f28a0f59	Unreachable code	t
0b6d1256-09fc-4f6a-97dd-173d3fac46d8	5f04f6ee-6902-471d-a17f-3521f28a0f59	Redundant code	t
2262be75-dc94-40c0-86cf-64907732a2bb	5f04f6ee-6902-471d-a17f-3521f28a0f59	Unused code	t
29baff50-656b-4069-a02b-81d4440f4ecf	5f04f6ee-6902-471d-a17f-3521f28a0f59	Dead variable	f
00045ba9-2974-4da1-8325-9d024db7fbf0	3c2c0705-7f3b-4e01-8eed-b7007495895c	1	f
10b0379f-d59d-4b65-a857-aa7e5e884997	3c2c0705-7f3b-4e01-8eed-b7007495895c	2	t
89a7b6ad-08b2-4987-be73-023574c6bc0d	3c2c0705-7f3b-4e01-8eed-b7007495895c	3	f
ed29097d-36af-4ef1-a0d6-774c3fa3964a	3c2c0705-7f3b-4e01-8eed-b7007495895c	4	f
6a6a7015-739f-430c-a0ee-3af7dfd52909	fac1e92e-f735-45a5-aee6-9c253b0c5de2	It can be used to describe the syntax of a programming language	f
550bdef4-02de-4242-8913-f7b6974b450a	fac1e92e-f735-45a5-aee6-9c253b0c5de2	It can be used to describe the semantics of a programming language	t
d2fb89f9-5cb3-48f6-8b8e-870e162647e6	fac1e92e-f735-45a5-aee6-9c253b0c5de2	It can be parsed using a top-down parser	f
255bf307-9bc7-4572-b30d-0caf9b26f4b4	fac1e92e-f735-45a5-aee6-9c253b0c5de2	It can be parsed using a bottom-up parser	f
de619f52-b317-47f7-aac3-e7333e6aa883	8b4f7e94-30b9-46fc-a427-b6b0f4e49702	Top-down parsing	f
b1e0e3e6-6c5f-4887-8dbd-683eaef951fd	8b4f7e94-30b9-46fc-a427-b6b0f4e49702	Bottom-up parsing	f
a334d274-2cb6-4a3b-8ce5-77313ac9c45c	8b4f7e94-30b9-46fc-a427-b6b0f4e49702	LL(1) parsing	f
1ef79cc5-402c-4723-b1de-422320b98893	8b4f7e94-30b9-46fc-a427-b6b0f4e49702	LR(1) parsing	t
d26516a6-8295-44f3-a50b-267fe43f8e43	990476ab-94b6-4810-b75e-94ebb0acdef4	It can parse a wider range of context-free grammars	t
a29b06e3-01ef-46b2-b221-056a3710b811	990476ab-94b6-4810-b75e-94ebb0acdef4	It is more efficient than a top-down parser	f
f9728faa-e8be-4813-af33-acc6ec3da0ff	990476ab-94b6-4810-b75e-94ebb0acdef4	It can handle left-recursive grammars	t
ecc26b10-596a-4694-a4bb-ea4e57369f4a	990476ab-94b6-4810-b75e-94ebb0acdef4	It can handle ambiguous grammars	f
b0e28a44-5f6d-4d8b-9bc8-b96dc11c655a	0fdcbe36-255c-428f-a017-b9ad944c89f7	It is responsible for parsing the syntax of a programming language	f
53648c0d-80af-4699-b602-00f3ce3416eb	0fdcbe36-255c-428f-a017-b9ad944c89f7	It is responsible for generating the intermediate code	f
d53ca9fa-2798-4eca-90fc-ee2ec8f7b6de	0fdcbe36-255c-428f-a017-b9ad944c89f7	It is responsible for recognizing tokens in the input string	t
f3a98c71-4f26-452d-a642-8b758bd38dbe	0fdcbe36-255c-428f-a017-b9ad944c89f7	It is responsible for optimizing the generated code	f
84cc9f47-3ceb-4d4b-8897-5cdfdbe51a38	edefd79b-90f6-4e62-bc9b-b7f88b550de4	Lexical analysis	t
fe58de0a-7776-4cef-b312-af4d3d436424	edefd79b-90f6-4e62-bc9b-b7f88b550de4	Syntax analysis	t
729b2e62-5476-4256-8577-6dcbb6a1a6c9	edefd79b-90f6-4e62-bc9b-b7f88b550de4	Semantic analysis	t
c7e552d2-c558-4e89-b99d-27ac137450e1	edefd79b-90f6-4e62-bc9b-b7f88b550de4	Code generation	t
\.


--
-- Data for Name: video_resources; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.video_resources (id, title, playlist_url, subject_id, is_deleted) FROM stdin;
4a04c51b-8719-4020-8bfb-0107249ea1f6	vishavdeep sir - os	https://youtube.com/playlist?list=PLG9aCp4uE-s17rFjWM8KchGlffXgOzzVP&si=qX-88OMZ1xBiCn-l	553dd23d-9091-4ba7-a892-d487101e9325	f
2af9c8fb-5b50-41d5-8f6c-df30e5c91d8e	khaleel sir - crash course	https://youtube.com/playlist?list=PL3eEXnCBViH-SiXK96TZd-7k3Qvk5g1YH&si=rzfnscpl44XRqdv1	553dd23d-9091-4ba7-a892-d487101e9325	f
ed1ab742-794f-46b3-89e4-cf89efc7dbc5	amit khurana	https://youtube.com/playlist?list=PLC36xJgs4dxEErKQZ7xFxat8oh4OepU34&si=M_GdGVyB8o4mSUh0	c5e1f1bd-f357-4c71-a9e7-4eb0590297c6	f
747a1087-d1d5-4c8d-b3b0-aeb95daaf5ad	chandan jha - crash course	https://youtube.com/playlist?list=PLOG_8OlGMp73cbcI1vw-q0I_IyjlsEhyI&si=GiJPnkqOI4jhUoik	c5e1f1bd-f357-4c71-a9e7-4eb0590297c6	f
d1ed8113-3144-46ac-bd1c-ab6d2fe5fb8f	ankit doyla sir	https://youtube.com/playlist?list=PLOG_8OlGMp73hMyn-WX1M2Q4ON98DmaRq&si=ySCeuJ-No0uvCIWx	643ec3ca-0a2b-4035-b165-0277b4c619b8	f
4c5d4f90-21a2-4653-89f9-d0dc4bf33f6d	deva sir - crash course	https://youtube.com/playlist?list=PL3eEXnCBViH_ePbZWc1nKZuyfru6sgioD&si=83oVRM-TayFFk01R	55f813b0-ff62-4639-8d1c-38526a0d465e	f
880f9f1a-414a-4c3a-b1da-6e4d05b63229	GO-Classes	https://youtube.com/playlist?list=PLIPZ2_p3RNHjy3eH_qRImIs5dVUTpr9ga&si=CS7wil5KmUJXoxwj	49c82e3e-c5a2-44c7-823b-b69c33560d8c	f
\.


--
-- Name: branches_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.branches_id_seq', 1, false);


--
-- Name: subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.subjects_id_seq', 1, false);


--
-- Name: video_resources_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.video_resources_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict je8UsEs5l6fdOImn01VoMGtSyB9hYeoWaUupjcsgye5bRVutQFF68I96q7V21dd

