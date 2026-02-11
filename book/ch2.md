# Slow Money

Social media connected five billion people. E-commerce went global — $6.4 trillion in online sales, a fifth of all retail on Earth. Work went remote overnight — Zoom went from 10 million daily users to 300 million in three months. Information became free. Entertainment became instant. Communication became invisible.

But money? Money still moves like it's 1973.

At least across borders. At least for most of the world. And if you're reading this from a country with a stable currency and a bank account that works, you might not feel it. Your card swipes fine. Your Venmo sends. Your direct deposit lands on Friday. Everything seems to work.

It doesn't. It just seems like it does because you've never seen anything better.

This chapter is about seeing the broken thing clearly.

## The Fundamental Problem: Money Lives Inside Banks

Every bank maintains its own truth about who has what. Your bank has a ledger. Your employer's bank has a different ledger. Your landlord's bank has another. When money moves between them, it's not actually money moving — it's a reconciliation between institutions. Your bank tells their bank, their bank tells their bank, and somewhere down the chain, a number changes in a database.

This is not a bug. This is the architecture. Money was designed to be institutional. It was designed to live inside banks, behind walls, accessible only with permission — an account, an identity, a physical presence, a credit history.

The result: money can only move as fast as institutions let it, and only to people institutions approve of.

Every problem in this chapter traces back to that single architectural fact.

## The Pipes Are Scared

The backbone of international money movement is a system called SWIFT. It was built in 1973.

1973. The year the Sears Tower was completed. The year *The Exorcist* opened in theaters. Fifty-three years ago.

Here's how SWIFT works: it doesn't actually move money. It sends messages. Bank A in New York sends a message to Bank B in London: "Please move $200 from Account X to Account Y." Bank B checks its records, confirms the instruction, and tells Bank C in Lagos to credit the recipient. Each bank in the chain only trusts the next one, so every hop is a settlement checkpoint, a compliance verification, and an opportunity for someone to take a cut.

The result: 2-5 day settlement times. Multiple intermediary banks. Opaque fees — the sender often doesn't know the final cost until the money arrives. If it arrives. Miss the cut-off window on Friday, wait until Monday. And that's for the transactions that go smoothly.

The system is not just old. It's shrinking. Over 20% of correspondent banking relationships have been cut globally since 2011 — banks dropping connections to other banks because the cost of AML compliance outweighs the revenue from serving small markets. Small countries like Tonga and Liberia have had their correspondent banking links severed entirely, cutting them off from the global financial system. Pacific island nations lost all banking connections.

Even SWIFT itself knows the pipes are breaking. They launched SWIFT gpi for faster tracking. They experimented with blockchain interoperability through Chainlink in 2023. The pipes are scared.

Deutsche Bank estimates that fintech and crypto solutions could grab $50-100 billion in annual correspondent banking revenues by 2030. A Latin American bank ran a test: sending $100,000 via stablecoin took 2 minutes and cost $0.20. The same amount via correspondent wire took 2 days and cost $550 in fees and intermediary charges. One transaction, same money, same people. Thousand-to-one difference.

And it's not just private companies routing around SWIFT. China's payment system, CIPS, linked with Russia's SPFS to bypass SWIFT entirely. China-Russia trade hit $218 billion in 2024 with a growing share settled in yuan and rubles, completely outside the Western financial plumbing. Governments are routing around the system too.

## The $58 Billion Tax on Poverty

Global remittances in 2024: $905 billion. Average fee: 6.4%. That's $58 billion a year extracted from the working class — from Filipino nurses in Dubai, from Guatemalan construction workers in Houston, from Zimbabwean teachers in London.

For over a century, the business model has been simple: charge a staggering fee to the people who can least afford it.

Intra-African fees often top 10% — among the highest globally. A worker in Johannesburg sending money to her family in Harare can lose a tenth of her paycheck to the transfer. The US-Mexico corridor moves $68 billion annually, with billions lost to fees. Gulf-to-South Asia corridors drain Filipino, Indian, and Pakistani workers in the UAE.

The people who can least afford fees pay the most. And they wait the longest. Days-long waits. Limited pickup locations. Restricted hours. A Filipino worker in Dubai sends money home and the chain looks like this: exchange house takes a cut, correspondent bank takes a cut, FX conversion takes a cut, receiving bank takes a cut, family gets what's left 3-5 days later.

Even the incumbents admit the system is broken. Western Union launched a stablecoin — USDPT on Solana — in 2025. Their CEO said it would "fundamentally reshape how money moves worldwide." MoneyGram now offers cash-to-USDC conversion in over 180 countries through its agent network on Stellar. The largest and oldest money-movers in the world have publicly conceded their own rails are broken.

26% of US migrants surveyed have used crypto for remittances. In Latin America, crypto-based remittances grew 40% year-over-year in 2023.

## 1.4 Billion People Don't Exist

Financially speaking.

1.4 billion adults globally have no bank account. Millions more are technically "banked" but can't access basic services — dormant accounts, minimum balance requirements they can't meet, branches too far away to reach.

The requirements to exist in the modern financial system: a physical branch visit, a government-issued ID, a minimum deposit, a credit history, an employment record, a residential address. If you lack any of these, you don't exist. Not to the bank. Not to the payment system. Not to the global economy.

The exclusion is structural. It's not profitable for banks to serve the last mile. Setting up a branch in rural Bihar or a small town in Malawi costs more than the deposits would generate. So they don't. And the people who live there are left with cash — physical, vulnerable, uninvested, earning nothing.

Mobile money was a partial answer. M-Pesa revolutionized Kenya — 66 million users, financial transactions via SMS. But M-Pesa is still siloed. It requires telco permission. It's national, not global. Try sending money from M-Pesa in Kenya to a bank account in Nigeria. You can't.

## Inflation as Silent Theft

In Buenos Aires, an Argentine teacher described converting her pesos to stablecoins as "stepping from a shaky boat onto solid ground."

Argentina: over 100% annual inflation. Your savings, halved in a year. Strict capital controls make buying physical US dollars nearly impossible through official channels.

Venezuela: hyperinflation made the bolivar essentially worthless for daily life. Pablo Toro, the delivery driver we met in the last chapter, left Caracas because his salary as a security guard couldn't buy groceries. In Bogota, he sends money home through a crypto app because "bank deposits sharply depreciate in weeks or even days."

Turkey: the lira lost over half its value in two years. A college student in Istanbul set up a USDT wallet for his grandmother after her pension kept losing purchasing power. She became a fan of the "dijital dolar."

Lebanon: the banking crisis froze withdrawals. Citizens couldn't access their own money. Mothers safeguarded medicine money in USDT.

Nigeria: a bank employee named Temi — who works at one of the country's top banks — secretly stashes her personal savings in USDT. "Inflation is eating away the value of the naira, meaning my savings and investments in naira are worthless." A bank employee doesn't trust her own bank.

In all of these countries, citizens have no opt-out within the traditional system. You are trapped in your currency unless you are rich enough to hold assets abroad. The psychological toll is real — people describe hyperinflation as watching their life's work melt. Converting to stablecoins is described as "therapeutic." "When I put my pesos into USDC, I can finally breathe. I know my money will be the same value next week."

This isn't financial analysis. It's survival.

## "But We Have Venmo"

Fair point. Some countries have built genuinely great domestic payment systems.

UPI in India: 12 billion transactions in a single month, zero fee to consumers. PIX in Brazil: 89% of adults used it, cut merchant costs by 85% versus card payments. FedNow in the US: near-real-time domestic clearing for about $0.045 per transaction.

These are real achievements. For domestic payments with good banking access, they work beautifully.

But none of them cross borders. PIX "lacks cross-border functionality" by design. FedNow stops at the water's edge. UPI requires SWIFT intermediaries to go international. And none of them solve inflation hedging, permissionless access, programmability, or the unbanked problem.

The insight from the research is actually surprising: stablecoins and these domestic systems are more complementary than competitive. The future might look like this: UPI converts rupees to a stablecoin, the stablecoin crosses the border in seconds, PIX converts it to reais on the other side. Stablecoins as the glue between domestic systems. Mastercard is already piloting exactly this.

While crypto aimed to bypass banks, its greatest payment impact might be augmenting the existing financial plumbing to be more interoperable.

## The $200 Journey

Here is what happens when a woman in New York sends $200 to her cousin in Lagos today, through the traditional correspondent banking system.

She walks into a money transfer office on a Tuesday afternoon. She fills out a form. She shows her ID. She hands over $200 in cash, plus a $12 fee.

Her $200 enters the system.

**Hop 1:** The transfer company's US bank receives the funds. They hold the money overnight because the cut-off time for outgoing wires was 3pm and it's now 3:47pm. Processing begins Wednesday morning. The bank charges a $5 handling fee internally.

**Hop 2:** The US bank sends a SWIFT message to its correspondent bank in London — because there's no direct relationship between this particular US bank and any Nigerian bank. The London bank receives the message on Wednesday, processes it Thursday morning (there was a queue), and deducts a £3 intermediary fee.

**Hop 3:** The London bank sends a SWIFT message to a correspondent bank in Lagos. This takes another day because of time zone differences and compliance checks. The Lagos correspondent receives the instruction Friday morning.

**Hop 4:** The Lagos correspondent bank converts the remaining USD to naira at its own exchange rate — which is worse than the market rate by about 2%. It sends the converted naira to the recipient's bank.

**Hop 5:** The recipient's bank receives the naira deposit and places a hold — standard procedure for incoming international transfers. The hold lasts until Monday.

**Hop 6:** Monday morning, the funds clear. The cousin receives a notification. She goes to the bank. She waits in line. She withdraws what's left.

Five days. Six institutions. Each one took a cut or added a delay. The original $200, after the initial fee, the intermediary fees, the FX markup, and the holds: **$174.**

$26 gone. And that's a clean transaction — no errors, no rejected wires, no compliance flags that freeze the transfer for an additional week of investigation.

Now here's the same $200, same people, on Stellar.

The woman in New York opens an app. She converts $200 to USDC. The app sends the USDC to her cousin's wallet address in Lagos. The blockchain fee is a fraction of a cent. Settlement time: 4 seconds.

Her cousin receives a notification on her phone. She opens her wallet. She sees $198 in USDC — $2 total for the on-ramp and off-ramp combined. She taps "convert to naira," and the money hits her mobile wallet or bank account within minutes.

Same money. Same people. Same Tuesday.

**$174 in five days versus $198 in four seconds.**

The gap should feel obscene. Because it is.

## The Punchline

We built a global real-time network for cat videos and memes in the 1990s.

We connected five billion people on social media. We put $6.4 trillion in commerce online. We made it possible to video call someone on the other side of the planet for free while walking down the street.

And we still move money like it's 1973. At least across borders. At least for the billions who need it most.

Individual countries have modernized domestically. But the cross-border system, the permissionless access, the inflation escape hatch — those are still broken. Money is the last major information system that hasn't been put on a shared, open, global ledger.

The gap between the dream in Chapter 1 and the reality in this chapter should feel offensive.

It should.

Because there's a bridge.
