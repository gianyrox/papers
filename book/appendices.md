# Appendices

## Jargon Decoder

**Core Concepts**

- **Stablecoin:** A digital token designed to maintain a stable value, typically pegged 1:1 to a traditional currency like the US dollar. A dollar that lives on the internet instead of in a bank.
- **Peg:** The target price a stablecoin aims to maintain — usually $1.00.
- **Depeg:** When a stablecoin's market price drifts away from its target. USDC trading at $0.87 is "depegged."
- **Fiat:** Government-issued currency — dollars, euros, naira, pesos. Money that has value because the government says it does.
- **Blockchain:** A distributed digital ledger that records transactions across many computers. No single entity controls it. Once recorded, entries are extremely difficult to alter.
- **Ledger:** A record of financial transactions. In traditional finance, each bank maintains its own private ledger. A blockchain is a shared ledger visible to all participants.

**How Stablecoins Work**

- **Reserves / Collateral:** The assets an issuer holds to back each stablecoin. For USDC, mostly US Treasury bills and cash. For DAI, other crypto assets locked in smart contracts.
- **Fully backed:** Every stablecoin in circulation has $1 of real assets behind it.
- **Over-collateralized:** More than $1 of collateral for each $1 of stablecoin issued. MakerDAO requires $1.50+ in ETH to mint $1 of DAI.
- **Algorithmic stablecoin:** Maintains its peg through code and incentives rather than reserves. TerraUST was the most famous — and its $40B collapse showed the limits of this approach.
- **Attestation vs Audit:** An attestation is a snapshot — an accountant confirms reserves at one moment. An audit is comprehensive — independent examiners verify all financial records over a period. Tether has only done attestations, never a full audit.
- **Smart contract:** Self-executing code on a blockchain that automatically enforces rules. A vending machine: put in the inputs, get the outputs, no human needed.
- **Authorized participant (AP):** A large financial institution with a direct agreement with a stablecoin issuer to mint (create) and redeem (destroy) tokens at par value. APs keep the price at $1.00 through continuous arbitrage.
- **Mint / Burn:** Creating (minting) or destroying (burning) stablecoin tokens. When you deposit $100 with Circle, they mint 100 USDC. When you redeem, they burn the USDC and return your dollars.
- **Seigniorage:** The profit earned from issuing currency — the difference between the face value and the cost of production. In stablecoins, this typically means the interest earned on reserves.

**Using Stablecoins**

- **On-ramp:** Converting traditional money into stablecoins. The "entrance" from the old financial system to the new one.
- **Off-ramp:** Converting stablecoins back to local currency or cash. Currently the hardest part in many countries.
- **Wallet (self-custodial):** An app that stores your private keys. You hold the keys, you hold the money. Lose the keys, lose the money.
- **Wallet (custodial):** A service like Coinbase that holds your stablecoins for you. Easier to use, but you're trusting the service.
- **Private key:** A cryptographic code that gives the holder control over a blockchain wallet. Whoever holds the private key controls the funds.
- **P2P (peer-to-peer):** Direct trading between individuals via a marketplace with escrow. How most people in Nigeria, Venezuela, and other restricted markets buy stablecoins.
- **Gas fee / Network fee:** The cost of processing a transaction on a blockchain. Fractions of a cent on Stellar and Solana. Several dollars on Ethereum during congestion.

**The Ecosystem**

- **DeFi (Decentralized Finance):** Financial services built on smart contracts instead of banks. Lending, borrowing, trading, insurance. Anyone can participate. Runs 24/7.
- **CeFi (Centralized Finance):** Crypto financial services operated by centralized companies — like Celsius, BlockFi, and FTX — where a company takes custody of user funds. CeFi collapsed spectacularly in 2022.
- **TVL (Total Value Locked):** The total dollar value in DeFi protocols. Roughly $230 billion as of Q3 2025.
- **Yield / APY:** Interest rate earned by depositing stablecoins. 2-8% in legitimate protocols. If someone offers 20%+, be suspicious.
- **Layer 2 / L2:** A secondary network built on top of a blockchain like Ethereum to process transactions faster and cheaper.
- **Bridge:** A protocol that moves tokens between different blockchains. Historically the biggest security vulnerability in crypto.
- **Flash loan:** A loan that is borrowed and repaid within a single blockchain transaction — typically lasting seconds. Used for arbitrage and, infamously, governance attacks.
- **Governance token:** A token that grants holders voting rights over a protocol's parameters and treasury.
- **Oracle:** A service that feeds real-world data (like asset prices) to smart contracts on a blockchain. DeFi protocols rely on oracles to know what assets are worth.
- **CBDC (Central Bank Digital Currency):** A digital currency issued by a government's central bank. Like a stablecoin but government-controlled. Examples: China's e-CNY, Nigeria's eNaira.
- **Liquidity pool:** A pool of tokens locked in a smart contract that enables decentralized trading. Users deposit tokens and earn fees from trades.
- **Liquidation:** The automatic selling of collateral when its value drops below a required threshold. In DeFi lending, if your collateral loses too much value, the protocol sells it to repay your loan.

**Stablecoin Types**

- **Fiat-backed:** Backed by real dollars (or other fiat currency) held in bank accounts and Treasury bills. USDC, USDT, PYUSD.
- **Crypto-collateralized:** Backed by cryptocurrency assets locked in smart contracts. DAI (backed by ETH and other assets).
- **Commodity-backed:** Backed by physical commodities. PAXG and XAUT are backed by physical gold.
- **Synthetic:** Track the value of an asset without holding it directly. sUSD on Synthetix.
- **Basket-pegged:** Pegged to a basket of currencies or assets rather than a single currency. Silk by Secret Network.

**Regulatory Terms**

- **GENIUS Act:** US federal law (2025) creating a framework for stablecoin issuers. Requires full reserves, monthly attestations, and consumer protections.
- **MiCA (Markets in Crypto-Assets):** EU regulation (2024) requiring stablecoin issuers to be licensed, maintain reserves, and meet transparency standards. Classifies stablecoins as EMTs (Electronic Money Tokens) or ARTs (Asset-Referenced Tokens).
- **KYC (Know Your Customer):** Identity verification requirements before using a financial service.
- **AML (Anti-Money Laundering):** Rules requiring monitoring and reporting of suspicious transactions.
- **Regulatory sandbox:** A controlled testing environment set up by a regulator that allows startups to test products under relaxed requirements.
- **BitLicense:** New York State's license for businesses engaging in virtual currency activities, issued by NYDFS.

**Historical / Economic Terms**

- **Bretton Woods:** The 1944 international monetary agreement that established the US dollar as the world's reserve currency, pegged to gold. Ended by Nixon in 1971 but the dollar's dominance persisted.
- **Eurodollars:** US dollars held in banks outside the United States, beyond the direct regulatory reach of the Federal Reserve. A multi-trillion-dollar market integral to global finance.
- **Gresham's Law:** "Bad money drives out good." When two currencies coexist, people spend the depreciating one and hoard the stable one. In stablecoin contexts, people spend naira and save USDT.
- **Thiers' Law:** The reverse of Gresham's: in extreme conditions (hyperinflation), good money drives out bad as people refuse to accept the depreciating currency.
- **Metcalfe's Law:** The value of a network is proportional to the square of the number of its users. Explains why stablecoin adoption accelerates once it reaches critical mass.
- **Hayek's Denationalization of Money (1976):** Friedrich Hayek's thesis that private issuers, driven by profit and reputation, would offer more stable money than monopolist governments.
- **Correspondent banking:** The arrangement where one bank provides international payment services on behalf of another. The intermediary chain that makes cross-border transfers slow and expensive.
- **Remittance corridor:** A specific geographic route along which money flows regularly between two countries.
- **M-Pesa:** Kenya's mobile money transfer service (launched 2007), which revolutionized financial access in East Africa. The name comes from "M" for mobile and "pesa," the Swahili word for money.

---

## The Machine: Who's Building It

A reference directory of the stablecoin ecosystem as of early 2026.

**Issuers — the new "central banks"**

| Issuer | Stablecoin | Key Facts |
|---|---|---|
| Tether | USDT | Dominant globally. ~$193B in assets. Controversial history. #1 by volume. |
| Circle | USDC | Enterprise-friendly. BlackRock manages reserves. Monthly reserve reports. |
| Paxos | PYUSD (for PayPal) | White-label stablecoin services. Powers PayPal's stablecoin. |
| MakerDAO | DAI | Community-governed. Backed by diversified collateral including $500M+ in Treasuries. |
| PayPal | PYUSD | First stablecoin from a major US financial firm. Launched August 2023. |

**Payment Networks**

| Company | Stablecoin Activity |
|---|---|
| Visa | USDC settlement pilot on Solana and Ethereum. $3.5B annualized volume. |
| Mastercard | Exploring stablecoin settlements. Piloting cross-border stablecoin integration. |
| Stripe | USDC payouts in 60+ countries. $1B crypto acquisition (Bridge). |
| MoneyGram | Cash-to-USDC in 180+ countries via Stellar. |
| Western Union | USDPT on Solana. 500,000+ physical locations as hybrid off-ramp. |

**Tech Giants**

| Company | Stablecoin Activity |
|---|---|
| Sony | Planning USD stablecoin for PlayStation ecosystem. Pursuing US banking charter. |
| Google | AP2 (Agentic Payment Protocol) for AI-to-AI stablecoin payments. |
| Coinbase | x402 protocol. Major USDC distribution partner. |
| WhatsApp / Telegram | Stablecoin transfer pilots in select markets. |

**Banks**

| Bank | Stablecoin Activity |
|---|---|
| JP Morgan | JPM Coin — $300B processed. Institutional on-chain settlement. |
| BNY Mellon | Custodying USDC reserves. |
| Société Générale | EUR stablecoin (EURCV) on Ethereum. |
| Goldman Sachs | Diginex platform experiments. Strategic Circle investor. |

**Infrastructure**

| Category | Key Players |
|---|---|
| Custody | BitGo, Fireblocks, Anchorage Digital |
| Compliance | Chainalysis, Elliptic, TRM Labs |
| On/off ramps | MoonPay, Transak, Ramp Network |
| Oracles & verification | Chainlink (oracles, Proof of Reserve) |
| Cross-chain | Circle CCTP, LayerZero, Wormhole |

**Blockchain Rails**

| Chain | Role in Stablecoin Ecosystem |
|---|---|
| Ethereum + L2s | Dominant ecosystem. DeFi hub. |
| Tron | 50%+ of USDT volume. Workhorse for emerging markets. |
| Solana | High-frequency trading and merchant payments. |
| Stellar | Purpose-built for payments. MoneyGram integration. |
| Celo | Mobile-first. Stablecoins for developing markets. |

**VC Capital**

Major investors: a16z (MakerDAO, Celo), BlackRock (Circle reserves, strategic investment), Fidelity and Visa (Circle's $9B valuation round), Goldman Sachs (Circle investor).

---

## UX Walkthroughs: How to Actually Use Stablecoins

Five step-by-step walkthroughs for different use cases. Each one follows a real persona through a complete transaction.

### Maria — Sending Money Home (US → Philippines)

**Who she is:** Maria is a nurse in Houston, Texas. She sends $300 to her parents in Cebu, Philippines every month. Western Union used to take $21 in fees and 3-5 days.

**Step 1: Get USDC.** Maria downloads Coinbase on her phone. She links her US bank account (takes 1-2 days for verification). She buys $300 in USDC. Coinbase charges no fee for USDC purchases from a linked bank account.

**Step 2: Send.** Maria opens her Coinbase app, taps "Send," and enters her father's wallet address in Cebu. She sends $300 USDC on the Stellar network. Fee: less than $0.01. Settlement: ~5 seconds.

**Step 3: Receive.** Maria's father receives a notification on his GCash app (which integrates with Stellar via MoneyGram). He sees $300 USDC in his wallet.

**Step 4: Off-ramp.** Maria's father walks to a local pawnshop that's a GCash/MoneyGram partner. He converts USDC to Philippine pesos. The off-ramp fee is approximately 1%. He receives ~$297 worth of pesos.

**Total cost:** ~$3 (1% off-ramp). **Time:** Under 10 minutes.
**Old way:** $21 fee + $300 = $279 received. 3-5 days.

**Common pitfalls:** Make sure the wallet address is correct — blockchain transactions are irreversible. Start with a small test amount ($10) the first time. Confirm off-ramp availability in the recipient's area before sending large amounts.

---

### Ramon — Hedging Against Inflation (Argentina)

**Who he is:** Ramon is a teacher in Buenos Aires, Argentina. His salary arrives in pesos, which lose value weekly. He converts what he can to stablecoins to preserve purchasing power.

**Step 1: Buy USDC via local exchange.** Ramon uses Belo or Lemon Cash — Argentine fintech apps that support stablecoin purchases. He deposits pesos via bank transfer or debit card. He buys USDC at the "blue dollar" rate (the unofficial parallel exchange rate).

**Step 2: Hold.** Ramon keeps USDC in the Belo app (custodial wallet). For larger amounts he wants to secure long-term, he transfers to a self-custodial wallet like MetaMask or Phantom.

**Step 3: Earn yield (optional).** If Ramon wants to earn interest, he can deposit USDC into Aave or Compound via his MetaMask wallet. Current rates: 4-6% APY. He understands this involves smart contract risk.

**Step 4: Spend or convert back.** When Ramon needs pesos for rent or groceries, he sells USDC on Belo for pesos deposited to his bank account. Some merchants in Buenos Aires accept stablecoin payments via QR code through Belo.

**Safety tips:** Never put all savings in one stablecoin or one app. Diversify between USDC and USDT. Understand that self-custodial wallets require you to secure your own private key — lose it and the funds are gone. Argentine tax treatment of crypto is evolving; consult local guidance.

---

### Chidi — Paying a Chinese Supplier (Nigeria)

**Who he is:** Chidi imports consumer electronics from Shenzhen, China. His bank can only provide a fraction of the USD he needs for supplier payments.

**Step 1: Buy USDT via P2P.** Chidi opens Binance and navigates to the P2P marketplace. He posts a buy order for USDT, offering naira via bank transfer. A seller matches his order. Chidi sends naira to the seller's bank account. The seller releases USDT from Binance escrow to Chidi's wallet.

**Step 2: Send to supplier.** Chidi's supplier in Shenzhen provides a Tron wallet address (typically via WeChat). Chidi sends USDT on the Tron network. Fee: less than $0.10. Settlement: ~1 minute.

**Step 3: Supplier confirms.** The supplier sees USDT arrive in their wallet and confirms the order. Shipment preparation begins.

**Step 4: Supplier off-ramps (optional).** The supplier can hold USDT, convert to CNY through a Chinese crypto exchange, or use OTC desks that serve Shenzhen's export community.

**Common pitfalls:** P2P trading carries counterparty risk — only trade with verified sellers with high completion rates. Use Binance's escrow system; never release funds outside the platform. Be aware of Nigerian regulations regarding crypto-to-fiat conversions. Keep records of all transactions for tax and compliance purposes.

---

### Mika — Receiving Stablecoin Payroll (US/Philippines)

**Who she is:** Mika is a UX designer based in the US who freelances for international clients. She receives payment in USDC.

**Step 1: Set up a wallet.** Mika downloads Phantom (a Solana-compatible wallet) and creates an account. She backs up her recovery phrase and stores it securely offline.

**Step 2: Invoice in USDC.** Mika sends her client an invoice with her Phantom wallet address and specifies USDC on Solana as the payment method. Some clients use Parallax or Request Finance for structured payroll disbursement.

**Step 3: Receive payment.** USDC arrives in her Phantom wallet — typically within seconds of the client sending it. No PayPal hold. No 3-5 business day processing. No 2.9% + $0.30 fee.

**Step 4: Off-ramp to bank.** Mika connects her Phantom wallet to Coinbase. She sends USDC from Phantom to her Coinbase account. She then sells USDC for USD and withdraws to her linked bank account. Coinbase typically processes this within 1-2 business days.

**Tax note:** Under current IRS guidance, receiving USDC as payment is a taxable event at the fair market value at the time of receipt. Converting USDC to USD may trigger a separate taxable event if there's been any change in value. Mika uses crypto tax software to track her cost basis and generate tax reports.

---

### Aisha — Running a Savings Club (Kenya)

**Who she is:** Aisha leads a 15-member savings club (chama) in Nairobi, Kenya. The group saves collectively and rotates payouts monthly.

**Step 1: Members contribute via M-Pesa.** Each member sends their monthly contribution (e.g., 5,000 KES) to Aisha via M-Pesa — Kenya's ubiquitous mobile money platform.

**Step 2: Convert to cUSD.** Aisha uses Kotani Pay — a service that bridges M-Pesa and blockchain — to convert the pooled Kenyan shillings to cUSD (Celo's dollar-pegged stablecoin). Celo was designed for mobile-first use; transactions are linked to phone numbers.

**Step 3: Hold in cUSD.** The pooled funds sit in Aisha's Celo wallet as cUSD. Unlike Kenyan shillings, the value doesn't erode with local inflation. Aisha can check the balance anytime on her phone.

**Step 4: Distribute.** When it's a member's turn to receive the payout, Aisha converts the necessary cUSD back to KES via Kotani Pay and sends it to the recipient's M-Pesa account. The recipient receives shillings on their phone.

**Safety tips:** Aisha keeps records of every transaction in a shared Google Sheet visible to all members. She starts with a small pilot month ($50 equivalent) before moving the full group's funds. She diversifies between cUSD and USDC if possible. She verifies Kotani Pay's exchange rates against market rates before each conversion.

---

## Open Questions

These are genuinely unanswered questions — not rhetorical devices, but real intellectual frontiers.

**On the dollar question:**

- If digital dollarization accelerates, what happens to countries that lose monetary sovereignty?
- Can non-USD stablecoins ever achieve network effects, or does the dollar's first-mover advantage make this a one-way door?
- When Tether holds $147 billion in US Treasuries, does a private BVI company get a seat at the table of monetary policy?

**On privacy and control:**

- Can privacy and compliance genuinely coexist through zero-knowledge proofs, or is "zkKYC" a contradiction in terms?
- If stablecoin issuers can freeze any wallet, how is this different from banking? If they can't, how do you stop laundering?

**On systemic risk:**

- At what market cap does a stablecoin crisis become a traditional market crisis?
- If stablecoins become the settlement layer for global trade, does a smart contract bug become a national security event?

**On the human question:**

- Do stablecoins help the poorest unbanked — people without smartphones or internet — or primarily the "underbanked" who already have digital access?
- If stablecoins make it easy to move money across borders, do capital controls become unenforceable?

**On the future:**

- Will stablecoins become invisible infrastructure — like TCP/IP — or remain a conscious user choice?
- Do stablecoins end up as a temporary bridge until CBDCs mature, or as permanent infrastructure?
- If the incumbents capture stablecoin rails, does it matter that the technology was decentralized?

---

## What Should You Do?

This book is informational and argumentative. But you'll finish it asking: "OK, so what do I actually DO?"

No specific product endorsements. General categories and principles. Not financial advice.

### If you live in a high-inflation country

- Buy your first stablecoin through a reputable exchange or P2P marketplace. Start small — $10-20 — to learn the process.
- Understand the difference between self-custody (you hold the keys) and custodial (an exchange holds them). Both have trade-offs.
- Evaluate safety: fully backed > algorithmic. Transparent reserves > opaque.
- Know your off-ramp: how to convert back to local currency when you need to.
- Diversify: never put all savings in one stablecoin.

### If you're a freelancer or small business

- Explore accepting stablecoin payments from international clients. Stripe and PayPal now support USDC natively.
- Understand the tax implications in your jurisdiction. Track cost basis on stablecoin receipts.
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

## Selected Bibliography

**Academic & Economic Theory**

- Hayek, F.A. (1976). *The Denationalisation of Money*
- Suri, T. & Jack, W. (2016). "The long-run poverty and gender impacts of mobile money." *Science*, 354(6317)
- Cengiz, F. (2025). "Stablecoins and the Hayekian Model." *Journal of International Economic Law*
- Luther, W. (AIER). "Network Effects and Money"
- Kocherlakota, N. (1998). "Money Is Memory." *Journal of Economic Theory*
- Kahneman, D. & Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*
- Schmandt-Besserat, D. (1992). *Before Writing: From Counting to Cuneiform*
- Cohen, E. (1992). *Athenian Economy and Society: A Banking Perspective*
- Quinn, S. & Roberds, W. (2014). "The Bank of Amsterdam through the Lens of Monetary Competition." Federal Reserve Bank of Atlanta

**Institutional Reports**

- BIS Annual Report 2025: "A unified ledger for correspondent banking"
- BIS Working Paper (May 2025, rev. Feb 2026): "Stablecoins and Safe Asset Prices"
- IMF, Duffie et al. (F&D 2025): "Compliance by Design" — zkKYC framework
- IMF, Finance & Development (Dec 2025): Stablecoin risks for emerging markets
- Atlantic Council (Jul 2025): "Stablecoin issuers as 3rd-largest buyer of US T-bills"
- Council on Foreign Relations (Aug 2025): "Dollar Stablecoins and the China Challenge"
- World Bank Remittance Prices Worldwide (quarterly)
- World Bank Global Findex Database 2021
- Edelman Trust Barometer 2026
- Wharton Stablecoin Toolkit (2026)
- FDIC, "How America Banks" (2023)
- Financial Stability Board: Stablecoin systemic risk reports (2023-2025)
- Tether, "Q4 2025 Financial Figures Report"
- US Bureau of Labor Statistics: CPI data (historical)

**Legislation & Regulation**

- GENIUS Act (US, June 2025)
- MiCA (EU, effective mid-2024)
- Brazil Lei 14,478 (December 2022)
- India Finance Act 2022 (crypto taxation)
- Nigeria SEC Virtual Asset Service Provider framework (2025)

**Industry Analysis**

- a16z: "State of Crypto" (2024, 2025)
- Chainalysis: Global Crypto Adoption Index (annual)
- McKinsey: "Digital finance could add $3.7T to emerging economy GDP"
- Bloomberg Intelligence: "$2.8T stablecoin supply by 2030"
- Morgan Stanley: "Modernizing Financial Infrastructure" (2025)
- Flagship Advisory Partners: "Decoding the Stablecoin Opportunity"
- AIER, Salter & Glazier (Sep 2025): "What Shipping Containers Did for Trade"
- Yellow Card Africa Report 2025
- Cato Institute: Stablecoin velocity analysis

**Journalism & Long-Form**

- Rest of World: Nigerian stablecoin adoption stories (2021-2025)
- Bloomberg: Argentine stablecoin economy (Oct 2025)
- Financial Times / Economist: Turkey stablecoin data (2024)
- Al Jazeera / Reuters: Venezuelan remittance stories (2021)
- Cambridge African Studies Review: Nigerian import trade (2025)
- Vice: Terra collapse human impact (May 2022)
- Wall Street Journal: Tether DOJ investigation (Oct 2024)
- Fortune: "Stablecoins Will Shake Up the $900 Billion Remittance Market" (Sep 2025)
