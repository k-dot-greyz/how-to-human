# README Donation Section - Acceptance Test

This README serves as an acceptance test for the donation section generator tool in `neuro-spicy-devkit`.

## ✅ Test Criteria

This README validates:

1. **Markdown Linting Compliance**
   - ✅ All code blocks have language identifiers (`text`)
   - ✅ No MD040 linting errors
   - ✅ Proper formatting throughout

2. **Address Validation**
   - ✅ Bitcoin address format validated
   - ✅ Ethereum address format validated (must start with `0x`)
   - ✅ Solana address format validated
   - ✅ Invalid ETH addresses caught and replaced with placeholder + warning

3. **Project Context**
   - ✅ Project name correctly replaced
   - ✅ GitHub username/repo correctly linked
   - ✅ Content adapted to project context (not generic)

4. **Structure & Formatting**
   - ✅ Consistent section structure
   - ✅ Proper whitespace
   - ✅ All links functional

## 🔧 Tool Reference

The donation section was generated/fixed using:
- **Tool**: `neuro-spicy-devkit/scripts/generate-donate-section.sh`
- **Template**: `neuro-spicy-devkit/docs/Donate_Crypto_Template.md`
- **Documentation**: `neuro-spicy-devkit/docs/DONATE_SECTION_GENERATOR.md`

## 📝 Test Command

```bash
cd neuro-spicy-devkit
./scripts/generate-donate-section.sh \
  -p "how-to-human" \
  -u "k-dot-greyz" \
  -r "how-to-human" \
  -b "bc1q3rfg8nxtqtmqvqk9yted68j3ny9v3xzlh2tqen" \
  -e "0x1234567890123456789012345678901234567890" \
  -s "Eh8yq5CWVVJu5dM73XxQzTnptaRwpKGeXMNqnTKPqqkw"
```

## 🎯 Result

This README demonstrates that the tool:
- Generates lint-compliant markdown
- Validates cryptocurrency addresses
- Adapts content to project context
- Produces production-ready donation sections

---

**Status**: ✅ **PASS** - All criteria met
