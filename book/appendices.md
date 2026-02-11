# Appendices

## Jargon Decoder

**Core Concepts**

- **Stablecoin:** A digital token designed to maintain a stable value, typically pegged 1:1 to a traditional currency like the US dollar. A dollar that lives on the internet instead of in a bank.
- **Peg:** The target price a stablecoin aims to maintain — usually $1.00.
- **Depeg:** When a stablecoin's market price drifts away from its target. USDC trading at $0.87 is "depegged."
- **Fiat:** Government-issued currency — dollars, euros, naira, pesos. Money that has value because the government says it does.

**How Stablecoins Work**

- **Reserves / Collateral:** The assets an issuer holds to back each stablecoin. For USDC, mostly US Treasury bills and cash. For DAI, other crypto assets locked in smart contracts.
- **Fully backed:** Every stablecoin in circulation has $1 of real assets behind it.
- **Over-collateralized:** More than $1 of collateral for each $1 of stablecoin issued. MakerDAO requires $1.50+ in ETH to mint $1 of DAI.
- **Algorithmic stablecoin:** Maintains its peg through code and incentives rather than reserves. TerraUST was the most famous — and its $40B collapse showed the limits of this approach.
- **Attestation vs Audit:** An attestation is a snapshot — an accountant confirms reserves at one moment. An audit is comprehensive — independent examiners verify all financial records over a period. Tether has only done attestations, never a full audit.
- **Smart contract:** Self-executing code on a blockchain that automatically enforces rules. A vending machine: put in the inputs, get the outputs, no human needed.

**Using Stablecoins**

- **On-ramp:** Converting traditional money into stablecoins. The "entrance" from the old financial system to the new one.
- **Off-ramp:** Converting stablecoins back to local currency or cash. Currently the hardest part.
- **Wallet (self-custodial):** An app that stores your private keys. You hold the keys, you hold the money. Lose the keys, lose the money.
- **Wallet (custodial):** A service like Coinbase that holds your stablecoins for you. Easier to use, but you're trusting the service.
- **P2P (peer-to-peer):** Direct trading between individuals via a marketplace with escrow. How most people in Nigeria, Venezuela, and other restricted markets buy stablecoins.
- **Gas fee / Network fee:** The cost of processing a transaction on a blockchain. Fractions of a cent on Stellar and Solana. Several dollars on Ethereum during congestion.

**The Ecosystem**

- **DeFi (Decentralized Finance):** Financial services built on smart contracts instead of banks. Lending, borrowing, trading, insurance. Anyone can participate. Runs 24/7.
- **TVL (Total Value Locked):** The total dollar value in DeFi protocols. Roughly $230 billion as of Q3 2025.
- **Yield / APY:** Interest rate earned by depositing stablecoins. 2-8% in legitimate protocols. If someone offers 20%+, be suspicious.
- **Layer 2 / L2:** A secondary network built on top of a blockchain like Ethereum to process transactions faster and cheaper.
- **Bridge:** A protocol that moves tokens between different blockchains. Historically the biggest security vulnerability in crypto.
- **CBDC (Central Bank Digital Currency):** A digital currency issued by a government's central bank. Like a stablecoin but government-controlled. Examples: China's e-CNY, Nigeria's eNaira.

**Regulatory Terms**

- **GENIUS Act:** US federal law creating a framework for stablecoin issuers. Requires full reserves, regular audits, and consumer protections.
- **MiCA (Markets in Crypto-Assets):** EU regulation requiring stablecoin issuers to be licensed, maintain reserves, and meet transparency standards.
- **KYC (Know Your Customer):** Identity verification requirements before using a financial service.
- **AML (Anti-Money Laundering):** Rules requiring monitoring and reporting of suspicious transactions.

---

## Open Questions

These are genuinely unanswered questions — not rhetorical devices, but real intellectual frontiers. They're invitations to think, not failures of analysis.

**On the dollar question:**

- If digital dollarization accelerates, what happens to countries that lose monetary sovereignty? Is the freedom to hold dollars worth the collective cost of abandoning your own currency?
- Can non-USD stablecoins ever achieve network effects, or does the dollar's first-mover advantage make this a one-way door?
- When Tether holds $141 billion in US Treasuries, does a private BVI company get a seat at the table of monetary policy?

**On privacy and control:**

- Can privacy and compliance genuinely coexist through zero-knowledge proofs, or is "zkKYC" a contradiction in terms?
- If stablecoin issuers can freeze any wallet, how is this different from banking? If they can't, how do you stop laundering?
- When governments can see every CBDC transaction and private companies can freeze any stablecoin — who do you trust less?

**On systemic risk:**

- At what market cap does a stablecoin crisis become a traditional market crisis?
- If stablecoins become the settlement layer for global trade, does a smart contract bug become a national security event?

**On the human question:**

- Do stablecoins help the poorest unbanked — people without smartphones or internet — or primarily the "underbanked" who already have digital access?
- If stablecoins make it easy to move money across borders, do capital controls become unenforceable? And is that liberation or chaos?

**On the future:**

- Will stablecoins become invisible infrastructure — like TCP/IP — or remain a conscious user choice?
- Do stablecoins end up as a temporary bridge until CBDCs mature, or as permanent infrastructure?
- If the incumbents capture stablecoin rails, does it matter that the technology was decentralized? Is "banking with better plumbing" a revolution or a renovation?

---

## What Should You Do?

This book is informational and argumentative. But you'll finish it asking: "OK, so what do I actually DO?"

No specific product endorsements. General categories and principles. Not financial advice.

### If you live in a high-inflation country

- Buy your first stablecoin through a reputable exchange or P2P marketplace. Start small — $10-20 — to learn the process.
- Understand the difference between self-custody (you hold the keys) and custodial (an exchange holds them). Both have trade-offs.
- Evaluate safety: fully backed > algorithmic. Transparent reserves > opaque. Published attestations > promises.
- Know your off-ramp: how to convert back to local currency when you need to.
- Diversify: never put all savings in one stablecoin. Spread across USDC, USDT, and DAI if possible.

### If you're a freelancer or small business

- Explore accepting stablecoin payments from international clients. Stripe and PayPal now support USDC natively.
- Understand the tax implications in your jurisdiction. Track cost basis on stablecoin receipts. Use crypto tax software.
- Legitimate yield on idle stablecoins exists. If it promises more than 10%, be suspicious.

### If you're sending money to family abroad

- Compare stablecoin remittance apps against your current method. Check total cost: on-ramp + blockchain fee + off-ramp.
- Confirm that the recipient can convert to local currency. The off-ramp matters more than the send.
- Total fees should be under 3%. If they're higher, shop around.

### If you're just curious

- Hold $10 in USDC for a week. Send it to a friend. Experience the speed and cost.
- Read the reserve reports. Circle publishes monthly. Tether publishes quarterly attestations.
- Follow the regulation. GENIUS Act, MiCA, your country's framework.
- Remember: a stablecoin is not an investment. It's a dollar on a different ledger.

### What NOT to do

- Don't chase yield above 8-10% APY. If it seems too good to be true, it is. Terra offered 20%.
- Don't put life savings in a single stablecoin or protocol.
- Don't ignore tax obligations.
- Don't assume "stable" means "risk-free." Understand what backs your stablecoin.
- Don't use a stablecoin wallet without understanding how to recover it if your phone is lost.

---

## 100 Stablecoin Opportunities: A Curated Map

The full list of 100 stablecoin company opportunities — spanning payments, banking, trade, emerging markets, DeFi, insurance, privacy, infrastructure, enterprise, and creative use cases — is available in the online companion at [companion URL].

Below is a curated selection of the highest-impact opportunities:

**Payments:** Global remittance platform, merchant payment gateway, stablecoin debit cards, micropayments for content

**Banking:** Stablecoin neobank, interest-bearing savings, lending platform, multi-currency wallet for travelers

**Trade:** Cross-border B2B settlement, supply chain payments, trade finance, forex service for businesses

**Emerging Markets:** Local currency stablecoins, mobile money integration, agent networks for cash conversion, micro-loans for unbanked

**DeFi:** Cross-chain stablecoins, yield aggregators, inflation-indexed stablecoins, decentralized lending

**Infrastructure:** Fiat-to-stablecoin onramps, developer APIs ("Stripe for stablecoins"), analytics platforms, global settlement networks

**Enterprise:** Corporate treasury management, interbank settlement, government payment platforms, global payroll

**Creative:** Gaming economies, IoT micropayments, content monetization, AI agent payments, carbon credit trading

Each one represents a piece of the old financial system being rewired. Not startup ideas — a map of everything that breaks, shifts, or reorganizes once stablecoins become base money.

---

## Selected Bibliography

**Academic & Economic Theory**

- Hayek, F.A. (1976). *The Denationalisation of Money*
- Suri, T. & Jack, W. (2016). "The long-run poverty and gender impacts of mobile money." *Science*, 354(6317)
- Cengiz, F. (2025). "Stablecoins and the Hayekian Model." *Journal of International Economic Law*
- Luther, W. (AIER). "Network Effects and Money"
- Kocherlakota, N. (1998). "Money Is Memory." *Journal of Economic Theory*

**Institutional Reports**

- BIS Annual Report 2025: "A unified ledger for correspondent banking"
- IMF, Duffie et al. (F&D 2025): "Compliance by Design" — zkKYC framework
- Atlantic Council (2025): "Stablecoin issuers as 3rd-largest buyer of US T-bills"
- World Bank Remittance Prices Worldwide (quarterly)
- Edelman Trust Barometer 2026
- Wharton Stablecoin Toolkit (2026)

**Industry Analysis**

- a16z: "State of Crypto 2024"
- Chainalysis: Global Crypto Adoption Index (annual)
- McKinsey: "Digital finance could add $3.7T to emerging economy GDP"
- Bloomberg Intelligence: "$2.8T stablecoin supply by 2030"
- Morgan Stanley: "Modernizing Financial Infrastructure" (2025)
- Flagship Advisory Partners: "Decoding the Stablecoin Opportunity"

**Journalism & Long-Form**

- Rest of World: Nigerian stablecoin adoption stories (2021-2025)
- Bloomberg: Argentine stablecoin economy (Oct 2025)
- Financial Times / Economist: Turkey stablecoin data (2024)
- Al Jazeera / Reuters: Pablo Toro and Venezuelan remittances (2021)
- Cambridge African Studies Review: "Femi" and Nigerian import trade (2025)
- Artemis Analytics: Mika Reyes interview (Feb 2025)

**Key Data Sources**

- World Bank Findex 2021: 1.4B unbanked adults globally
- Yellow Card Africa Report 2025: Nigerian stablecoin adoption data
- Cato Institute: Stablecoin velocity analysis
- AIER, Salter & Glazier (Sep 2025): "What Shipping Containers Did for Trade"
- WEF (Jan 2026): "How Stablecoins Can Expand Financial Access"
