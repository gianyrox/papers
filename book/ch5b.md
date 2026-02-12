## The Steel-Manned Case Against Stablecoins

These are the best arguments from the smartest critics, stated at their strongest. The book's credibility depends on engaging with them directly. Seven arguments. The answers vary — some are clear, some are uncomfortable, and one has no clean resolution at all.

---

### "This Is Dollar Imperialism With Better UX"

Over 99% of stablecoins are USD-pegged.[^1] When a Nigerian farmer saves in USDT instead of naira, he makes a rational individual choice. But collectively, millions making that same choice is de facto dollarization[^2] — and it strips developing nations of monetary sovereignty, seigniorage[^3] revenue, and the ability to respond to local economic shocks with local monetary policy.

The IMF warned in 2025 that "the growing embrace of stablecoins comes with under-acknowledged risks for poorer nations. Their influx has further weakened local currencies, reducing central banks' ability to conduct effective policy."[^4]

When the Fed raises rates, the whole world already feels it through trade channels. Stablecoins add a new transmission mechanism: hundreds of millions of people holding dollar instruments that respond to Fed policy directly, not mediated through local banks.

Non-USD stablecoins are less than 1% of the market and show no sign of catching up.[^5]

The Eurodollar[^6] parallel is instructive. In the 1960s, US dollars accumulated in European banks outside American regulation. These "Eurodollars" were initially viewed with suspicion. They became integral to global finance. The US eventually supported them because they entrenched dollar dominance without requiring American institutions to be present in every market. The consequences played out over decades in ways nobody predicted — including the 2008 crisis, where offshore dollar lending amplified the contagion.

Stablecoins are Eurodollars 2.0 — the same offshore dollar proliferation dynamic, except this time it's not institutional banks holding them. It's citizens. And that makes the dependency harder to reverse.

**The counter:** For people in countries with 100%+ inflation, the alternative to dollarization is watching their savings evaporate. An Argentine teacher converting her pesos to USDC isn't choosing dollar imperialism. She's choosing to eat next month. A Zimbabwean savings club converting to cUSD isn't undermining monetary sovereignty — Zimbabwe's monetary sovereignty was undermined by its own central bank printing the currency into worthlessness.

The tension is real. Individual rationality creates collective dependency. But the people making these choices don't have the luxury of waiting for their central banks to get it right. The question is whether the ecosystem can develop non-USD alternatives — euro stablecoins, local-currency stablecoins, IMF SDR-pegged instruments — fast enough to provide choices beyond the dollar. So far, it hasn't. That's a problem worth tracking, not a reason to deny people access to stable money while tracking it.

---

### "If They Can Freeze Your Money, This Isn't Freedom"

Vitalik Buterin — the creator of Ethereum, the most credible voice in the crypto ecosystem — put this directly: "If major stablecoins like USDC were to blacklist addresses or choose sides in a fork, it would give them enormous power over Ethereum."[^7]

He's right. And it's already happening.

Circle and Tether have frozen over 800 addresses combined, often at law enforcement request.[^8] When Tornado Cash was sanctioned, Circle blacklisted 81+ addresses and froze roughly $75,000 in USDC.[^9] Your "self-custodied" digital dollars can be rendered worthless with one smart contract call.

The centralization is structural, not incidental. Fiat-backed stablecoins REQUIRE a centralized issuer who holds reserves and can freeze tokens. Decentralized alternatives have catastrophically failed (Terra, Iron Finance). The choice appears to be: centralized stablecoin that can freeze you, or decentralized stablecoin that might collapse to zero.

So how is this different from a bank freezing your account? You've traded one centralized authority for another — one subject to your local law, the other subject to US law you have no voice in.

**The counter is a spectrum, not a binary.** DAI — a decentralized stablecoin created by MakerDAO — has operated since 2017 without collapsing and without a centralized freeze capability.[^10] It's smaller than USDT or USDC, and it's not fully decentralized (it holds USDC as collateral), but it exists as proof that the design space is wider than "centralized or broken." Zero-knowledge compliance is emerging — systems where regulatory requirements are met through cryptographic proofs rather than centralized control.

And even centralized stablecoins offer improvements over banking for the 1.4 billion people who can't get a bank account at all. 24/7 access. No minimum balance. No credit check. Global portability. For someone who has never had a financial account to freeze, a freezable stablecoin is still an upgrade over nothing.

The discomfort here is real: the ecosystem currently trends toward more centralization, not less. Whether it moves toward privacy-preserving designs depends on demand and regulation. That direction is not guaranteed.

---

### "The Truly Unbanked Can't Use This"

Stablecoins require a smartphone, internet access, and enough technical literacy to manage a wallet. The "1.4 billion unbanked" includes many people who lack reliable internet, a smartphone, or digital literacy. MoneyGram's 180-country agent network is real but thin in rural areas. Brazil's 24,000 crypto ATMs are concentrated in cities. The deepest poverty is correlated with the least digital access.

This argument is valid today. The question is the trajectory.

Smartphone penetration in Sub-Saharan Africa grows roughly 10% annually.[^11] M-Pesa IS integrating stablecoins across 8 countries, bringing its existing agent network — people, not apps, in physical locations — to bear.[^12] GCash in the Philippines has 66 million users and is integrating with Stellar for USDC cashouts at pawnshop agents.[^13] In the Philippines, you can walk into a 7-Eleven and convert cash to crypto through ECPay.

The pattern is the same one that played out with mobile money itself. Urban first. Then rural, as demand proved the business model. M-Pesa took five years to reach 50% of Kenyan adults. The timeline is compressing — not because the technology is better, but because the infrastructure (phones, agents, apps) already exists from the mobile money wave.

Stablecoins don't have to reach everyone to be transformative. If they reach the 2-3 billion people who have smartphones but don't have good banking, that's already a paradigm shift. The remaining gap is real and matters — but it's a digital access problem, not a stablecoin problem. And it's closing.

---

### "DeFi Yields Are Just Rehypothecated Risk"

Anchor Protocol offered 20% APY and attracted $18 billion in deposits.[^14] It was a Ponzi. Celsius offered 8-18% and was lending recklessly. BlockFi, Voyager — all collapsed. The pattern: centralized yield products attract depositors with unsustainable rates, use funds for risky bets, and blow up. Even "legitimate" yields come from leverage — someone is borrowing at 5-10% to speculate, and when the music stops, liquidation cascades follow.

Agustín Carstens, General Manager of the Bank for International Settlements, delivered the institutional verdict: "A technology doesn't make for trusted money."[^15]

He's making a broader point worth sitting with: the fact that stablecoins run on blockchains doesn't eliminate the old risks of finance. Leverage, fraud, unsustainable returns, hidden exposure — these are human problems, not technical ones. New rails don't fix old behavior.

**The distinction that matters:** CeFi[^16] and DeFi[^17] are fundamentally different, and collapsing them together is analytically wrong.

CeFi platforms — Celsius, BlockFi, Voyager, FTX — collapsed because they were opaque, under-collateralized, and run by humans making bad bets behind closed doors. They took customer deposits and gambled. When the bets went wrong, customers lost everything.

DeFi protocols — Aave, Compound, MakerDAO — survived the same crisis. They are transparent (all positions visible on-chain), over-collateralized (borrowers must deposit more value than they borrow), and enforce rules via code rather than human discretion. MakerDAO navigated a 70% price crash in March 2020 with zero bailouts.[^18] Aave V3 held $15 billion in liquidity through the 2022-2023 bear market.[^19]

The lesson from 2022 is not "yield is bad." It's "opaque, under-collateralized yield managed by humans behind closed doors is bad." That's the same lesson traditional finance taught in 2008. The rails are different; the risk management principles are identical.

Current DeFi lending rates on major protocols: 4-8% APY on stablecoin deposits.[^20] These rates come from transparent, over-collateralized borrowing — visible on-chain, liquidated automatically if collateral drops. They're real yields from real demand. Whether those rates persist in a lower-interest-rate environment is a fair question (see below). Whether they're Ponzi yields is not — the mechanism is auditable.

---

### "This Recreates the Same Power Structures"

Nouriel Roubini — the economist who predicted the 2008 crisis and has been the most vocal critic of the entire crypto ecosystem — does not mince words: "These stablecoin issuers are like wildcat banks. If we let them continue, it's only a matter of time before a crisis."[^21]

Here's his case. Tether earned over $13 billion in 2024 from the float — seigniorage that used to flow to governments.[^22] Circle, backed by BlackRock and Goldman Sachs, is the other dominant issuer. The "decentralized" stablecoin ecosystem is controlled by two companies, backed by Wall Street. Visa, Stripe, and PayPal are the on-ramps. JP Morgan is the custodian. You've rebuilt the banking system with extra steps and fewer consumer protections.

This is the most uncomfortable argument in the chapter because it contains substantial truth. The short-term trajectory IS toward institutional capture. Power is consolidating.

Two things are different from traditional banking. First: the rails are open. Anyone can build on them without permission. A Nigerian fintech can plug into USDC without getting a banking charter from four countries. Yellow Card built Africa's largest crypto exchange on public blockchain infrastructure that nobody had to approve. Second: the competition is global with lower barriers to entry. Will power consolidate? Probably. But in a more contestable way than traditional banking, where regulatory barriers to entry are the primary moat.

Roubini's "wildcat banking" comparison deserves a direct response. The free banking era of the 1800s produced hundreds of private currencies, many of which failed spectacularly. But it also produced the regulatory frameworks — reserve requirements, audits, deposit insurance — that stabilized the banking system. The GENIUS Act and MiCA are the 21st-century equivalents. The question is whether regulation arrives fast enough to prevent the crisis Roubini predicts. He may be right about the risk. The answer is better regulation, not prohibition.

---

### "Most of That Volume Is Crypto Trading, Not the Real Economy"

An estimated 88% of stablecoin transactions in 2024 were for crypto trading — not real-world commerce.[^23] Traders moving USDT between exchanges to arbitrage. DeFi protocols recycling capital through lending loops. Market makers minting and redeeming. Strip out the trading volume and the "real economy" stablecoin usage is a fraction of the headline $27.6 trillion.

The snapshot is accurate. Here's why the trend line matters more.

The 88% trading share was higher in 2021-22. It's declining as real-world use cases grow.[^24] SMB usage doubled from 17% to 34% between 2024 and 2025.[^25] Remittance flows, payroll, B2B settlement, and merchant payments are all growing faster than trading volume as a percentage of total.

The parallel is the early internet. In the 1990s, the overwhelming majority of internet traffic was academic and military. Commercial use was a rounding error. The infrastructure got built for one use case and adopted for others. By the time consumer adoption hit the S-curve, the network capacity and routing protocols built for research handled commercial traffic seamlessly.

Stablecoin infrastructure is following the same path. Trading built the liquidity, the on-ramps, the exchange integrations, the wallet ecosystems. Those same pipes now carry remittances and payroll. The $27.6 trillion headline includes the trading volume. The trajectory is toward a growing share of that number being real economic activity. Both facts are true. The book should state both honestly.

What strengthens this argument further: look at WHO is using stablecoins and WHERE. In Nigeria, 80% of stablecoin trades are under $1,000 — grassroots, not institutional arbitrage.[^26] In Argentina, 61% of crypto volume is stablecoins used for savings and commerce. Yellow Card reports stablecoins are 99% of transactions across its 20-country African network.[^27] The "mostly trading" argument applies globally but not in the markets where stablecoins matter most.

---

### "This Runs on 5% Treasury Yields — What Happens When Rates Drop?"

Tether earned over $13 billion in 2024.[^28] These profits are entirely a product of 5%+ Treasury yields. At 0.5% yields — where the US was from 2009 to 2021 — Tether's profit drops by roughly 90%. The VC interest, the new entrants, the institutional enthusiasm — all catalyzed by a specific interest rate environment that is cyclical, not permanent.

This is a clean, correct argument. The yield bonanza accelerated everything. It attracted entrants, funded expansion, and made the economics irresistible.

What it didn't create: the use cases. Nigerian traders using USDT to pay Chinese suppliers don't care about Tether's yield. Pablo's remittances work at any interest rate. Mercy's savings club protects against inflation regardless of what US Treasuries pay. The fundamental draw — instant, borderless, permissionless money movement — is rate-independent.

What IS rate-dependent: issuer profitability, yield product attractiveness, and the pace of institutional entry. Lower rates slow the business side without reversing the usage side. The risk isn't that stablecoins stop working. It's that lower rates cause issuers to cut corners — reduce transparency, chase riskier yields, take on more leverage — to maintain profitability. That's the scenario regulators should watch for. The GENIUS Act's reserve requirements are designed precisely to prevent it.

---

### The Environmental Question

One counterargument deserves a short answer because the facts have changed. The energy criticism that dogged Bitcoin for years is largely irrelevant for stablecoins.

Ethereum completed its "Merge" to proof-of-stake in September 2022, reducing energy consumption by 99.9%.[^29] A single Ethereum transaction now uses approximately 0.03 kWh — comparable to a Google search.[^30] Solana processes transactions at approximately 0.00051 kWh each.[^31] Tron and Stellar are similarly efficient.

The stablecoins running on these networks — USDC on Ethereum, USDT on Tron, cUSD on Celo — inherit their host chain's energy profile. The environmental cost of moving a stablecoin dollar is negligible compared to the infrastructure required to run a correspondent banking chain, operate physical branch networks, and maintain legacy settlement systems.

This doesn't eliminate all environmental concerns — data centers still consume power, and blockchain network effects could increase aggregate energy use. But the "crypto is boiling the ocean" framing doesn't apply to modern stablecoin infrastructure.

---

Seven arguments. None of them are easy to dismiss. Several contain real truth that the stablecoin ecosystem hasn't fully addressed. The dollar imperialism problem has no clean resolution. The power consolidation trend is real. The trading volume ratio is honest and unflattering.

This book's thesis survives these arguments — but only because the evidence for stablecoin utility is strong enough to carry the weight of its problems. For a Venezuelan family, a Nigerian trader, a Zimbabwean savings club, the counterarguments are real but the alternative is worse. The gains for billions of people outweigh the costs — provided regulation arrives fast enough to prevent the systemic risks the critics correctly identify.

That's a conditional thesis. It depends on execution. If Tether collapses before regulation matures, the critics will have been right. What that collapse looks like — and who pays the price — is the next section.

---

[^1]: As of Q4 2025, USDT and USDC alone account for over 90% of stablecoin market capitalization. Non-USD stablecoins (EUROC, XSGD, TRYB, etc.) are less than 1% of total value.

[^2]: Dollarization occurs when a country's citizens adopt a foreign currency (typically the US dollar) for savings and transactions, either officially or informally, reducing the role of the local currency.

[^3]: Seigniorage is the profit a government earns from issuing currency — the difference between the face value of money and the cost of producing it. When citizens hold stablecoins instead of local currency, seigniorage revenue shifts from governments to private stablecoin issuers.

[^4]: IMF, Finance & Development, December 2025.

[^5]: Chainalysis, "Geography of Cryptocurrency Report," 2024.

[^6]: Eurodollars are US dollars held in banks outside the United States, beyond the direct regulatory reach of the Federal Reserve. The Eurodollar market emerged in the 1960s and grew into a multi-trillion-dollar system integral to global finance.

[^7]: Vitalik Buterin, public statement on stablecoin centralization risks, 2023.

[^8]: Combined frozen address data from Circle and Tether transparency reports, as of Q4 2025.

[^9]: Circle blacklisted addresses associated with Tornado Cash following US Treasury OFAC sanctions, August 2022.

[^10]: MakerDAO and DAI have operated since December 2017. DAI maintains its dollar peg through over-collateralization with crypto assets and real-world assets.

[^11]: GSMA, "The Mobile Economy Sub-Saharan Africa," 2024.

[^12]: M-Pesa / Safaricom blockchain integration across Kenya, Tanzania, Mozambique, DRC, Ghana, Egypt, Lesotho, and Ethiopia. Announcements 2023-2025.

[^13]: GCash / Stellar / MoneyGram integration, Philippines, 2024.

[^14]: Anchor Protocol held approximately $18 billion in deposits at its peak, offering ~20% APY on UST deposits. It collapsed along with TerraUST in May 2022.

[^15]: Agustín Carstens, General Manager of the Bank for International Settlements, speech on stablecoins and monetary trust, February 2023.

[^16]: CeFi (Centralized Finance) refers to crypto financial services operated by centralized companies — like Celsius, BlockFi, and FTX — where a company takes custody of user funds and makes investment decisions on their behalf. Users must trust the company's solvency and honesty.

[^17]: DeFi (Decentralized Finance) refers to financial services built on public blockchains using smart contracts — like Aave, Compound, and MakerDAO — where rules are enforced by code, all positions are visible on-chain, and no single entity holds custody of user funds.

[^18]: MakerDAO survived the March 2020 crash (ETH dropped ~70% in hours) through automated liquidations. Some liquidations malfunctioned, but the system recovered without external bailout. MakerDAO post-mortem, 2020.

[^19]: Aave V3 total value locked and protocol performance data, DeFi Llama, 2023-2024.

[^20]: Aave and Compound stablecoin lending rates as of Q4 2025. Rates vary by market conditions and utilization.

[^21]: Nouriel Roubini, public remarks comparing stablecoins to wildcat banks, 2022-2023.

[^22]: Tether, "Q4 2025 Financial Figures Report." Tether reported net profit exceeding $13 billion for 2024, primarily from interest on US Treasury reserves.

[^23]: Visa / a16z analysis of stablecoin transaction composition, 2024.

[^24]: a16z, "State of Crypto Report," 2025. Real-economy stablecoin usage growing faster than trading as percentage of total volume.

[^25]: Industry survey data comparing 2024 and 2025 SMB stablecoin adoption rates.

[^26]: Yellow Card Africa Report, 2025. 25.9 million Nigerian users, 80% of transactions under $1,000.

[^27]: Chris Maurice, CEO of Yellow Card, Bloomberg, 2024.

[^28]: Tether, "Q4 2025 Financial Figures Report."

[^29]: Ethereum Foundation, "The Merge," September 15, 2022. Ethereum transitioned from proof-of-work to proof-of-stake, reducing network energy consumption by an estimated 99.95%.

[^30]: Ethereum Foundation energy consumption estimates post-Merge, 2023.

[^31]: Solana Foundation energy and sustainability report, 2023.
