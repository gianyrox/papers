# A Stablecoin Dystopia

The trust shift from "I trust my bank" to "I trust this mechanism" is only valid if we're honest about what mechanisms have failed and can still fail. This chapter is what separates a credible book from a promotional pamphlet.

## What's Already Broken

### The Collapse That Proved the Critics Right

May 2022. TerraUST — an algorithmic stablecoin backed not by dollars in a vault, but by a complex relationship with its sister token LUNA — lost its peg and entered a death spiral. In days, roughly $40 billion was vaporized: $18 billion in UST market cap and $22 billion in LUNA value.

The mechanism was supposed to be elegant: if UST dropped below $1, arbitrageurs would burn UST and mint LUNA, restoring the peg through supply reduction. But when confidence evaporated, the feedback loop reversed. More UST sold, more LUNA minted, LUNA crashed 99.99%, and the arbitrage couldn't keep up with the panic.

Anchor Protocol — a lending platform built on Terra — had attracted $18 billion in deposits by offering 20% APY on UST. Twenty percent annual return on what was marketed as a dollar. When new money stopped flowing in to sustain the yield, the system failed like a bank run meets a Ponzi scheme.

The contagion rippled outward. Three Arrows Capital became insolvent. Celsius froze customer withdrawals. The entire crypto credit market crumbled.

The human cost was staggering. A young trader in Colombia lost 100% of his life savings: "The guilt is unbearable. I've had big drawdowns before, but this time I'm zero, nothing." A disabled retiree living on $197 per month: "I'm not rich. So this hurts me." The Terra subreddit became a space of anguish — communities organized suicide prevention outreach for members expressing despair.

IMF Managing Director Georgieva: "When it's not backed with assets but promises 20% return, it's a pyramid. And what happens to pyramids? They eventually fall to pieces."

Money carries dreams and fears. When stablecoins fail, the emotional toll is devastating.

### The Catalog of Failures

Terra was the largest, but not the only one.

**Iron Finance / TITAN (June 2021):** A partial-collateral stablecoin — 75% USDC, 25% TITAN token. TITAN went from roughly $60 to $0 in a single day. Mark Cuban lost around $870,000 providing liquidity. A precursor warning to Terra that the community failed to heed.

**USDC (March 2023):** Circle disclosed $3.3 billion — 8% of reserves — was stuck at the collapsing Silicon Valley Bank. USDC fell to $0.87. $4.5 billion was redeemed in days — a modern digital bank run. It recovered when the FDIC backstopped SVB deposits. The lesson: even fully-backed stablecoins carry counterparty risk from the banking system they're supposed to replace.

**USDT:** Briefly hit roughly $0.95 during the May 2022 panic. Quickly recovered, but showed even the biggest stablecoin is vulnerable to confidence shocks. USDT also dipped to $0.97 in 2018 during solvency rumors.

**Beanstalk (April 2022):** A flash loan governance attack. An attacker used a momentary loan to accumulate 75% of governance votes, passed a proposal to drain roughly $182 million in collateral, and executed it in a single transaction. $77 million was laundered through Tornado Cash and never recovered. Bean crashed to $0.12. The lesson: even if the economic model is sound, operational security can zero you out.

**Cashio (March 2022):** An infinite mint exploit on Solana. A coding error allowed an attacker to mint 2 billion CASH tokens without collateral and redeem approximately $52.8 million in real assets. The attacker called himself a "Robin Hood." The protocol was abandoned.

**Cross-chain bridge hacks:** Roughly $2.5 billion stolen in bridge hacks between 2021 and 2023. Wormhole lost $325 million — an attacker minted wrapped ETH on Solana without locking real ETH on Ethereum. Jump Trading replaced the funds. Nomad lost $190 million in a chaotic exploit where hundreds of copycat attackers drained the protocol. Bridges are the weakest link — high-value targets with small multisig security or poorly audited code.

Not all of these failures are "crypto problems" in the way critics frame them. Terra was a bank run meets Ponzi. USDC was old-fashioned banking counterparty risk. Beanstalk and Cashio were code exploits. The diversity of failure modes shows that stabilizing value is genuinely hard. The only stablecoins that haven't broken their peg are fully fiat-backed — and even they've had moments of stress.

### Centralization and Censorship

Circle and Tether CAN and DO freeze wallet addresses. Over 800 combined, often at law enforcement request.

When Tornado Cash was sanctioned, Circle blacklisted 81+ addresses and froze roughly $75,000 in USDC — demonstrating that your "self-custodied" digital dollars can be rendered worthless with one smart contract call.

Tether has frozen over 700 addresses. Your "digital dollars" can be confiscated by the issuer. For users in sanctioned countries or using privacy tools, this is not a theoretical risk.

The philosophical tension is real: the promise of "money like cash" conflicts with the reality of centralized freeze capabilities. Rune Christensen, MakerDAO's founder: "The current design is too dependent on real-world assets like USDC. We need a stablecoin that can survive blacklisting and censorship — truly decentralized." But truly decentralized stablecoins have historically been the ones that collapse. The tension doesn't resolve cleanly.

### The Tether Problem

Tether is roughly $86 billion — two-thirds of all stablecoin value. "Too big to fail" for crypto markets, but with no one to bail it out.

$192.9 billion in assets versus $186.5 billion in liabilities, with $6.4 billion in excess reserves. Reserve composition: $141.6 billion in Treasury bills and overnight repo (safe), $17.4 billion in gold — quietly one of the world's largest gold holders — $8.4 billion in Bitcoin. But also: $17 billion in secured loans with undisclosed borrowers, up from $5 billion. The borrowers and collateral are unknown.

No full audit. Only quarterly attestations from a Cayman Islands accountant. Tether's own report acknowledges: "Our figures are a one-day attestation, not an audit." No Big-4 accounting firm has audited Tether. This keeps many institutions away.

Under DOJ investigation for potential bank fraud — no charges filed. Previous settlements: $42.5 million CFTC fine for misleading reserve claims, $18.5 million NYAG settlement, barred from operating in New York. At one point in 2017, Tether was found to have had "virtually no reserves."

On the other hand: Tether's CEO argues USDT is "the dollar for the last mile, for the unbanked." Almost the entire user base is in emerging markets. He frames Tether as "advancing US dollar hegemony across emerging markets."

Profitability: $9-10 billion in interest income in 2025. Net profits exceeding $10 billion. Revenue of $5.2 billion equaling 42% of all crypto protocol revenue. More profitable per employee than most global banks.

The stress test it passed: after FTX collapsed, Tether honored over $7 billion in redemptions within 48 hours without breaking the peg. It froze roughly $835 million in USDT related to crime.

The stress test it hasn't faced: what happens at scale. If Tether's reserves were found to be significantly short, or if a regulatory action froze its banking relationships, the forced liquidation of $141 billion in Treasury bills could spill into traditional markets. The FSB has warned about exactly this scenario.
