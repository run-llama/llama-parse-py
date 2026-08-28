# Changelog

## [2.15.0](https://github.com/run-llama/llama-parse-py/compare/v2.14.1...v2.15.0) (2026-08-28)


### Features

* **extract:** publish the turbo tier on the public API surface (LI-8873) ([32faf41](https://github.com/run-llama/llama-parse-py/commit/32faf411ea420a701df13034914d7da28d9f9b96))

## [2.14.1](https://github.com/run-llama/llama-parse-py/compare/v2.14.0...v2.14.1) (2026-08-20)


### Bug Fixes

* **parse:** restore inline_images on cost_effective (new version 2026-08-11) ([#23804](https://github.com/run-llama/llama-parse-py/issues/23804)) ([f9fb346](https://github.com/run-llama/llama-parse-py/commit/f9fb3468c94557915103103fa3a471cdae408d14))
* **python:** restore the API surface deleted by a stale-gen-head rebuild (LI-8886) ([dd487df](https://github.com/run-llama/llama-parse-py/commit/dd487df15393bfeb2596dfbae41e98269f9035fa))
* route security reports to support@runllama.ai; name LlamaIndex, Inc. in LICENSE ([#12](https://github.com/run-llama/llama-parse-py/issues/12)) ([f90563e](https://github.com/run-llama/llama-parse-py/commit/f90563e5dc10f8a1c433c286e03b4f0884731452))


### Chores

* seal the back-sync, promote and CHANGELOG state as custom code ([6551775](https://github.com/run-llama/llama-parse-py/commit/6551775dea45da3dd6cfd832e09f2d20473c9790))
* seal the LlamaIndex-owned release-doctor, LICENSE and SECURITY edits as custom code ([baa220a](https://github.com/run-llama/llama-parse-py/commit/baa220a032f93c2c7b61f202d9bb92b716cc1449))


### Documentation

* fix non-compiling README examples (LI-8881) ([8b50146](https://github.com/run-llama/llama-parse-py/commit/8b501460ea47804417c9cf71cc4d51a77a995555))

## [2.14.0](https://github.com/run-llama/llama-parse-py/compare/v2.13.0...v2.14.0) (2026-08-12)

> [!WARNING]
> **Breaking change:** `files.get()` is renamed to `files.content()`. It returns the presigned download URL, as before.
> `client.files.get(file_id)` no longer exists and raises `AttributeError` at runtime — replace it with `client.files.content(file_id)`.
> `client.files.retrieve(file_id)` returns the file resource itself.
> Released as a minor, not a major, because a major would force the sibling Go SDK's module path to `/v2`.


### Features

* **batches:** webhooks for /api/v2/batches ([#23148](https://github.com/run-llama/llama-parse-py/issues/23148)) ([f781ad3](https://github.com/run-llama/llama-parse-py/commit/f781ad394f63b7e4311cea3b2cfbfa329a59a918))
* **classify:** accept webhook_configuration_ids on classify job create (LI-8138) ([#22943](https://github.com/run-llama/llama-parse-py/issues/22943)) ([d598c7c](https://github.com/run-llama/llama-parse-py/commit/d598c7c7c815b5eb1cc6b8777e2f25d75ec896e6))
* **connector:** API + service layer for attaching a subscription to a directory ([#23502](https://github.com/run-llama/llama-parse-py/issues/23502)) ([cd905bb](https://github.com/run-llama/llama-parse-py/commit/cd905bb2d04ea7c08f2903d80e29d9a5b15233c1))
* **connectors:** expose a directory's connector subscription, and resolve connected accounts ([#23831](https://github.com/run-llama/llama-parse-py/issues/23831)) ([b6d9a60](https://github.com/run-llama/llama-parse-py/commit/b6d9a608661ea4ae49eea2ddf3af6c42e6affc5e))
* **extract:** accept webhook_configuration_ids on extract job create (LI-8138) ([#22907](https://github.com/run-llama/llama-parse-py/issues/22907)) ([aa6e771](https://github.com/run-llama/llama-parse-py/commit/aa6e77124a5ec2b76ecba80c78baec9c3fb41c27))
* **extract:** opt-in spreadsheet mode for agentic_plus ([#22958](https://github.com/run-llama/llama-parse-py/issues/22958)) ([d036ed0](https://github.com/run-llama/llama-parse-py/commit/d036ed00e66973c2c45333e685f44d4dfa402492))
* **extract:** pin turbo to a stable dated version; accept citations+confidence, reject only granular bboxes ([#22965](https://github.com/run-llama/llama-parse-py/issues/22965)) ([76130ca](https://github.com/run-llama/llama-parse-py/commit/76130ca09f4ba09944fa79f4ff7e2e36a6f2594b))
* **extract:** reject parse_tier for parse-free tiers + pin turbo fallback to fast ([#22919](https://github.com/run-llama/llama-parse-py/issues/22919)) ([b0d665f](https://github.com/run-llama/llama-parse-py/commit/b0d665fbf687bca819da68db6dcb65846b7b9306))
* **files:** rename files.get to files.content and restore files.retrieve ([db4a012](https://github.com/run-llama/llama-parse-py/commit/db4a012fe2d48f1f885b057d0fd97c53927890cb))
* **forms:** emit bboxes in v2 forms output ([#23974](https://github.com/run-llama/llama-parse-py/issues/23974)) ([1768b9b](https://github.com/run-llama/llama-parse-py/commit/1768b9b13a252e782f808b47bc0e7fd4ed92b74f))
* **parse,extract:** add expand=usage returning credits billed per job ([#23709](https://github.com/run-llama/llama-parse-py/issues/23709)) ([cb4716e](https://github.com/run-llama/llama-parse-py/commit/cb4716eeab5a8ea4d9e4dda18c9a22c25c760c14))
* **parse:** extract Word revision annotations ([#23152](https://github.com/run-llama/llama-parse-py/issues/23152)) ([07a0e62](https://github.com/run-llama/llama-parse-py/commit/07a0e62754064179b44b8bead25bc173b9dd9d2c))
* **parse:** make the output.pdf artifact opt-in on Parse v2 (output_options.save_output_pdf) ([#23510](https://github.com/run-llama/llama-parse-py/issues/23510)) ([7eb28a8](https://github.com/run-llama/llama-parse-py/commit/7eb28a8e1e3481ae50672b6563e3999fba2e7b4f))
* **split:** accept webhook_configuration_ids on split job create (LI-8138) ([#22940](https://github.com/run-llama/llama-parse-py/issues/22940)) ([460d643](https://github.com/run-llama/llama-parse-py/commit/460d6436f46a3d902da976737b812eadc35f809e))


### Bug Fixes

* absorb production main into staging to unblock the release loop ([a305233](https://github.com/run-llama/llama-parse-py/commit/a305233bacea930d8ef45ce3c7639698e8800376))
* **api:** name paginated + filter schemas instead of leaking generic parametrizations ([#23120](https://github.com/run-llama/llama-parse-py/issues/23120)) ([1eaeab3](https://github.com/run-llama/llama-parse-py/commit/1eaeab385484eb2c29550980733a360886e9c24b))
* **llamaparse:** retry qwen context-overflow 400s with a shrinking OCR anchor ([#23817](https://github.com/run-llama/llama-parse-py/issues/23817)) ([b1bb4e3](https://github.com/run-llama/llama-parse-py/commit/b1bb4e302c48df4cc45229281ea83b9082a0ef8d))


### Chores

* **api:** regenerate OpenAPI specs for new agentic parse version ([#22763](https://github.com/run-llama/llama-parse-py/issues/22763)) ([967ac03](https://github.com/run-llama/llama-parse-py/commit/967ac03e167b579d3c42b729c42be413283bbb4a))


### Documentation

* **parse:** shorten the images_to_save field description ([#23807](https://github.com/run-llama/llama-parse-py/issues/23807)) ([9a45754](https://github.com/run-llama/llama-parse-py/commit/9a45754378eff75cae783ff5badbc9cd68220d49))


### Refactors

* remove Depends(get_db) from permissions endpoints ([#22635](https://github.com/run-llama/llama-parse-py/issues/22635)) ([98f87c6](https://github.com/run-llama/llama-parse-py/commit/98f87c6a11b1da1fe7a0c5e26d475c7cc228979e))

## [2.13.0](https://github.com/run-llama/llama-parse-py/compare/v2.12.0...v2.13.0) (2026-07-22)


### Features

* **extract:** report num_pages_billed on extract job usage ([#22323](https://github.com/run-llama/llama-parse-py/issues/22323)) ([90b9a1b](https://github.com/run-llama/llama-parse-py/commit/90b9a1bd856de9168d4c956d21b9147eb7287fac))
* **sheets:** cost_effective/agentic tiers and per-region billing ([#22508](https://github.com/run-llama/llama-parse-py/issues/22508)) ([2cdb29c](https://github.com/run-llama/llama-parse-py/commit/2cdb29c269ceac27b427ce955310f386ebd660c1))

## [2.12.0](https://github.com/run-llama/llama-parse-py/compare/v2.11.0...v2.12.0) (2026-07-21)


### Features

* **gdrive:** reuse-first connection picker in the data-source connect modal ([#21725](https://github.com/run-llama/llama-parse-py/issues/21725)) ([dda7ac8](https://github.com/run-llama/llama-parse-py/commit/dda7ac8ba99f64bc3868bc48f75dfad1f3c509e6))
* **llamaparse:** agentic 2026-07-15 — Markdown-pipe table body for Gemini 3.1 Flash-Lite (EU primary) ([#22208](https://github.com/run-llama/llama-parse-py/issues/22208)) ([b3767d9](https://github.com/run-llama/llama-parse-py/commit/b3767d9ef0d17f2cd753ab78533b073b23aea1c3))
* **parse:** adding forms pass to api layer (forms=`enrich` param + output types) ([#22012](https://github.com/run-llama/llama-parse-py/issues/22012)) ([4239bbe](https://github.com/run-llama/llama-parse-py/commit/4239bbea84fde0a5c04dc8a19d474c63455ec548))
* **parse:** confidence_scores="verified" — per-page AI-verified confidence + document-level score ([#22083](https://github.com/run-llama/llama-parse-py/issues/22083)) ([7a4e1d1](https://github.com/run-llama/llama-parse-py/commit/7a4e1d176c136d16b4f7ce39c8c320e74686a153))
* **parse:** rename confidence scoring option + billing event (confidence_score_effort / confidence_score_high) ([#22290](https://github.com/run-llama/llama-parse-py/issues/22290)) ([c75005b](https://github.com/run-llama/llama-parse-py/commit/c75005b2a3c1d9011a97824859a9474667689254))


### Bug Fixes

* **parse:** declare the recursive form node schemas as models ([8b5208a](https://github.com/run-llama/llama-parse-py/commit/8b5208ae3c6e8c5d8dd18b91c314b03630475284))

## [2.11.0](https://github.com/run-llama/llama-parse-py/compare/v2.10.0...v2.11.0) (2026-07-09)


### Features

* **agentic-plus:** dated version 2026-07-08 — graduate decomposed-gemini (flash-lite), fallback to 2026-06-18 ([#21738](https://github.com/run-llama/llama-parse-py/issues/21738)) ([bed1c22](https://github.com/run-llama/llama-parse-py/commit/bed1c22675e570da9a9218576dfecb4a4eeeb9e3))
* update fast tier latest version to use liteparse + markdown ([#21669](https://github.com/run-llama/llama-parse-py/issues/21669)) ([7bd8a60](https://github.com/run-llama/llama-parse-py/commit/7bd8a60fbf5372d21bc0bc8b54534835261e4e92))


### Bug Fixes

* resolve conflict markers committed by the auto-resolver ([2749857](https://github.com/run-llama/llama-parse-py/commit/2749857bbb974935eff3d93d51615fc084cf4999))

## [2.10.0](https://github.com/run-llama/llama-parse-py/compare/v2.9.1...v2.10.0) (2026-06-30)


### Features

* **index:** add output_directory_id to IndexResponse ([#21149](https://github.com/run-llama/llama-parse-py/issues/21149)) ([7c33775](https://github.com/run-llama/llama-parse-py/commit/7c337754ac339bc66e407249a74a07bf1f632c71))


### Bug Fixes

* **ci:** make cli SDK push race-proof and self-heal the seal-back loop ([a44fa38](https://github.com/run-llama/llama-parse-py/commit/a44fa38b4ff92062fd66f0fa25096ea64dbab7f2))
* **python:** drop removed expires_at param from batch example; resolve parsing import conflict ([35ddf0b](https://github.com/run-llama/llama-parse-py/commit/35ddf0bbdde3046620df497e0b5b4c9240d01c63))


### Chores

* correct manifest to 2.9.1 (already on PyPI) and pin 2.10.0 ([7a11fdf](https://github.com/run-llama/llama-parse-py/commit/7a11fdf2bae486db8141e703b581a41ddf7fe62c))

## 2.9.0 (2026-06-09)

Full Changelog: [v2.8.0...v2.9.0](https://github.com/run-llama/llama-parse-py/compare/v2.8.0...v2.9.0)

### Features

* **api:** api update ([6c61a1f](https://github.com/run-llama/llama-parse-py/commit/6c61a1f4a5a28144eae31542bc711d6f70a29c61))
* **api:** api update ([a642524](https://github.com/run-llama/llama-parse-py/commit/a64252425eb9888c6c57c5fbbb4f17f7e95e88fc))
* **api:** api update ([5dfb1b0](https://github.com/run-llama/llama-parse-py/commit/5dfb1b097af2334d1bddcf70bc5e2a5b9f204834))
* **api:** api update ([95e5f08](https://github.com/run-llama/llama-parse-py/commit/95e5f08e7799e23f5167620ea1f65b73641d4005))
* **api:** api update ([5476040](https://github.com/run-llama/llama-parse-py/commit/54760400ca8e9401f4544801d7ca6f0fde69db36))
* **api:** api update ([d447ad5](https://github.com/run-llama/llama-parse-py/commit/d447ad52971deb8094ff0477fb14cecd6423c88e))


### Bug Fixes

* lint (exclude the file from basepyright checks) ([f2ebdaf](https://github.com/run-llama/llama-parse-py/commit/f2ebdaff2d3f09b2c9573bdaf685127314753fba))


### Chores

* exclude from mypy as well ([80a0727](https://github.com/run-llama/llama-parse-py/commit/80a072710af7aa38a6eb210fcbe583a894ebc49c))
* update SDK settings ([f5bdef2](https://github.com/run-llama/llama-parse-py/commit/f5bdef28a93f54d546e2627f0400ff355aa5d0d1))


### Documentation

* index v2 examples ([fa14309](https://github.com/run-llama/llama-parse-py/commit/fa14309abce3e8a3fdd13b7ef9283e31f099aa21))

## 2.8.0 (2026-05-28)

Full Changelog: [v2.7.0...v2.8.0](https://github.com/run-llama/llama-parse-py/compare/v2.7.0...v2.8.0)

### Features

* **api:** api update ([3c06bf0](https://github.com/run-llama/llama-parse-py/commit/3c06bf039ca9b3542cda0d6e0aef0c74892d3221))
* **api:** api update ([868fc0d](https://github.com/run-llama/llama-parse-py/commit/868fc0d40ab51bb8b61751480268c578fb24a3e9))
* **api:** batches support ([87522c3](https://github.com/run-llama/llama-parse-py/commit/87522c310d41f579e3ca994f96b1927be5c9dd40))

## 2.7.0 (2026-05-20)

Full Changelog: [v2.6.0...v2.7.0](https://github.com/run-llama/llama-parse-py/compare/v2.6.0...v2.7.0)

### Features

* **api:** api update ([211ccac](https://github.com/run-llama/llama-parse-py/commit/211ccac82c1607a168046b5df5b8e577d01f992d))
* **api:** api update ([7439110](https://github.com/run-llama/llama-parse-py/commit/7439110a10fc1480b11ea071a6d84df57d33b925))
* **api:** swap grep and file search to grep/find + pagination ([1ce1187](https://github.com/run-llama/llama-parse-py/commit/1ce1187927176d9883e314b8945eb02511725871))

## 2.6.0 (2026-05-19)

Full Changelog: [v2.5.0...v2.6.0](https://github.com/run-llama/llama-parse-py/compare/v2.5.0...v2.6.0)

### Features

* **api:** Adding in Resources For Retrieval and Chat ([2eb6e25](https://github.com/run-llama/llama-parse-py/commit/2eb6e25c258e71cc46110444a126bddf2c98eed3))
* **api:** api update ([f2171ca](https://github.com/run-llama/llama-parse-py/commit/f2171caf6c5e81045b1d6d7993e52a57a2c6ccad))
* **api:** Updating indexes endpoints within the sub resources. ([4a1b7ec](https://github.com/run-llama/llama-parse-py/commit/4a1b7ec0a652336a39be4545be365840c77e92e8))

## 2.5.0 (2026-05-14)

Full Changelog: [v2.4.1...v2.5.0](https://github.com/run-llama/llama-parse-py/compare/v2.4.1...v2.5.0)

### Features

* **api:** api update ([7bdde63](https://github.com/run-llama/llama-parse-py/commit/7bdde634068532ba84bd8125f5e6260cf63dc124))
* **api:** api update ([07665a9](https://github.com/run-llama/llama-parse-py/commit/07665a98d15a397cb685473fde620072c1dce536))
* **api:** api update ([d13afd9](https://github.com/run-llama/llama-parse-py/commit/d13afd9a2a5c64cee394b193da47f96b7a165db9))
* **api:** api update ([6a9cc96](https://github.com/run-llama/llama-parse-py/commit/6a9cc96e656984c84d5693a5d9800e1e2f9fbd53))
* **api:** api update ([8ab8bb9](https://github.com/run-llama/llama-parse-py/commit/8ab8bb903a51f8fc5719454dbcaa16423fdbc362))
* **internal/types:** support eagerly validating pydantic iterators ([b8000a4](https://github.com/run-llama/llama-parse-py/commit/b8000a4c445edd14503b13f341061cbf72ae3bb0))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([d01c276](https://github.com/run-llama/llama-parse-py/commit/d01c2767b61d27c9df6957676eeccee55632a7cf))


### Chores

* **internal:** reformat pyproject.toml ([d0ea3c0](https://github.com/run-llama/llama-parse-py/commit/d0ea3c05044133131c47025fc2a7cf0e659c1726))
* sync repo ([50348db](https://github.com/run-llama/llama-parse-py/commit/50348db551d45f34efc8d71f77a7452b9d15815d))
* update SDK settings ([06edb62](https://github.com/run-llama/llama-parse-py/commit/06edb6291c83a106f48c9ad82cad667baa611569))

## 2.4.1 (2026-04-17)

Full Changelog: [v2.4.0...v2.4.1](https://github.com/run-llama/llama-cloud-py/compare/v2.4.0...v2.4.1)

### Bug Fixes

* **api:** Also support agent data `.create` for consistency ([46656fa](https://github.com/run-llama/llama-cloud-py/commit/46656fa2fa257d8db3ce6aec7ff1ea174765055d))
* **beta:** re-add agent_data() alias for backwards compat ([#84](https://github.com/run-llama/llama-cloud-py/issues/84)) ([ff0efb0](https://github.com/run-llama/llama-cloud-py/commit/ff0efb0d84b8281d2ea6d9255cc45c55f4ddfc58))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([08182c5](https://github.com/run-llama/llama-cloud-py/commit/08182c581678d7a32412218edd315565c36a8eed))

## 2.4.0 (2026-04-16)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/run-llama/llama-cloud-py/compare/v2.3.0...v2.4.0)

### Features

* **api:** api update ([9ae910d](https://github.com/run-llama/llama-cloud-py/commit/9ae910d188ce74a3c34d3b0ca646f826dd571d8b))
* **api:** api update ([2ef67a1](https://github.com/run-llama/llama-cloud-py/commit/2ef67a11dba6bf311d8653a1ba9a48014178163a))
* **api:** api update ([fc7d45d](https://github.com/run-llama/llama-cloud-py/commit/fc7d45d5792e53c34b0606c5016b63fbf7b5dfe3))
* **classify:** add wait_for_completion and run() helpers ([#82](https://github.com/run-llama/llama-cloud-py/issues/82)) ([2e0feda](https://github.com/run-llama/llama-cloud-py/commit/2e0fedad3407ad270bc7fd2532bad2cb79cbd127))


### Bug Fixes

* ensure file data are only sent as 1 parameter ([7e8e651](https://github.com/run-llama/llama-cloud-py/commit/7e8e6519cb12b6cb2a0a896996563f63ce7614ea))


### Documentation

* update examples ([55dce5f](https://github.com/run-llama/llama-cloud-py/commit/55dce5f39923174d07b0ce87cc5633bfaa9a9333))

## 2.3.0 (2026-04-07)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/run-llama/llama-cloud-py/compare/v2.2.0...v2.3.0)

### Features

* **api:** remove parse configurations, superseded by generic configurations from 2.2.0 ([ef96778](https://github.com/run-llama/llama-cloud-py/commit/ef9677851bec9ffb3d1cfedd431efd881b3ef7f9))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([53c3d0a](https://github.com/run-llama/llama-cloud-py/commit/53c3d0aa13ccb9b3d6aa7b18c1943b52802c1aaa))
* use agentic parse for citation bounding box demo ([#78](https://github.com/run-llama/llama-cloud-py/issues/78)) ([4f0c201](https://github.com/run-llama/llama-cloud-py/commit/4f0c201b2f91e9d765d061a9450c6fce519585f2))

## 2.2.0 (2026-04-03)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/run-llama/llama-cloud-py/compare/v2.1.0...v2.2.0)

### Features

* **api:** Add product configurations ([e72b9dc](https://github.com/run-llama/llama-cloud-py/commit/e72b9dc79919794f1f5859b4b64147c158531951))


### Bug Fixes

* pin cookbook test file URLs to main merge commit hash ([#77](https://github.com/run-llama/llama-cloud-py/issues/77)) ([12c70b4](https://github.com/run-llama/llama-cloud-py/commit/12c70b4a43e6a978898bb849f96b506ddc76f540))


### Documentation

* **extract-v2:** complete walkthrough cookbook ([#61](https://github.com/run-llama/llama-cloud-py/issues/61)) ([e45ac66](https://github.com/run-llama/llama-cloud-py/commit/e45ac66f69f2ae11f51e66d24183459f49822a74))

## 2.1.0 (2026-04-01)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/run-llama/llama-cloud-py/compare/v2.0.0...v2.1.0)

### Features

* **api:** api update ([8d47ebf](https://github.com/run-llama/llama-cloud-py/commit/8d47ebfbe4428d5e8be9177f441c6923fd0bf583))
* **api:** api update ([06f4920](https://github.com/run-llama/llama-cloud-py/commit/06f49206aab97f1db1523bdd5d497ac604a8dcb1))

## 2.0.0 (2026-03-31)

Full Changelog: [v1.6.0...v2.0.0](https://github.com/run-llama/llama-cloud-py/compare/v1.6.0...v2.0.0)

### ⚠ BREAKING CHANGES

* remove extraction v1 resource, extract v2 metadata restructure

### Features

* add run() and wait_for_completion() convenience methods to extract resource ([e491e0e](https://github.com/run-llama/llama-cloud-py/commit/e491e0e3a2b04c9185b6ef0b2c3e9f59c2759be0))
* **api:** api update ([b55bf1d](https://github.com/run-llama/llama-cloud-py/commit/b55bf1d107484a77e5dac30dc81e9c12c05f4b2f))
* **api:** api update ([bd38c9d](https://github.com/run-llama/llama-cloud-py/commit/bd38c9d3ecd6660122d8f57b97214856507d38d6))
* **api:** api update ([6bb5ad6](https://github.com/run-llama/llama-cloud-py/commit/6bb5ad6f9affbaa8699dc743dcc08b4e58a2acc8))
* **api:** api update ([50db89d](https://github.com/run-llama/llama-cloud-py/commit/50db89da14d8c9145926642d5dd90b8b0303b88d))
* **api:** api update ([0778957](https://github.com/run-llama/llama-cloud-py/commit/077895773ff4e642708dc77d9232e02265f83a4e))
* **api:** api update ([11b99e9](https://github.com/run-llama/llama-cloud-py/commit/11b99e96c19891052e652c40a21749e8f5291701))
* **api:** api update ([7630e8f](https://github.com/run-llama/llama-cloud-py/commit/7630e8f00a765eefa993cd90aa0b9d2bf7172f9a))
* **api:** api update ([b0cd8ae](https://github.com/run-llama/llama-cloud-py/commit/b0cd8aec4e28ee607c31acf2e5ebea8c0b833b4b))
* **api:** api update ([c67b4d7](https://github.com/run-llama/llama-cloud-py/commit/c67b4d714c8b4019fda6749135fe52061d3f1414))
* **api:** api update ([00fbe28](https://github.com/run-llama/llama-cloud-py/commit/00fbe284d2f10866f7d9aa17858e5c2eddfa0bed))
* **api:** api update ([c8a2a3c](https://github.com/run-llama/llama-cloud-py/commit/c8a2a3cb25915a920d9dab1ec3aa5d7f6c152f32))
* **api:** api update ([a9ad222](https://github.com/run-llama/llama-cloud-py/commit/a9ad22276492e5e84c6ed8f361ed66fa9c0ca38d))
* **api:** api update ([56e6a2c](https://github.com/run-llama/llama-cloud-py/commit/56e6a2c9d500e66f3fe160deacc93a395637bf4a))
* **api:** manual updates ([952154c](https://github.com/run-llama/llama-cloud-py/commit/952154c93bf1a7a6917c9417f8b0f240cc5a992c))
* **internal:** implement indices array format for query and form serialization ([65757d5](https://github.com/run-llama/llama-cloud-py/commit/65757d5917a857c8d9fc8d0be8a03583f63b4bb9))
* remove extraction v1 resource, extract v2 metadata restructure ([379de20](https://github.com/run-llama/llama-cloud-py/commit/379de20160a2b3ac462829fdb20afda445c55d8d))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([75fe56d](https://github.com/run-llama/llama-cloud-py/commit/75fe56d34f5dcd23a180f3aa52bbccfca4412866))
* **pydantic:** do not pass `by_alias` unless set ([3f72991](https://github.com/run-llama/llama-cloud-py/commit/3f7299119d6d4f50e661eded3a986444c74117ab))
* sanitize endpoint path params ([1e60a1b](https://github.com/run-llama/llama-cloud-py/commit/1e60a1bdcfee2fd8478f384e4b107f08cc0f8eb3))
* sort imports in extract.py ([ac8ce5e](https://github.com/run-llama/llama-cloud-py/commit/ac8ce5eb0fe74b24d021491b626aa050411a153b))


### Chores

* **ci:** skip lint on metadata-only changes ([c0b8113](https://github.com/run-llama/llama-cloud-py/commit/c0b81135abd66c5681db1599ca9db4ad6e340ee0))
* **ci:** skip uploading artifacts on stainless-internal branches ([e18445d](https://github.com/run-llama/llama-cloud-py/commit/e18445da2c05ba4b1e0e135a2446266e69a584bf))
* **internal:** tweak CI branches ([35d72e9](https://github.com/run-llama/llama-cloud-py/commit/35d72e973c03dc643ca0024baffa79e43d789f9b))
* **internal:** update gitignore ([01210a2](https://github.com/run-llama/llama-cloud-py/commit/01210a2d96802057b35009fb26c3f4f53e3aaefa))
* update placeholder string ([a87a6a8](https://github.com/run-llama/llama-cloud-py/commit/a87a6a8915b4e911f6976954e3eaa60aae7fde4e))

## 1.6.0 (2026-03-05)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/run-llama/llama-cloud-py/compare/v1.5.0...v1.6.0)

### Features

* **api:** add better deprecation messages ([67d464b](https://github.com/run-llama/llama-cloud-py/commit/67d464b17ad38286fa67fe167f400a73f5ca937a))
* **api:** Add Classify V2 API ([48ecb15](https://github.com/run-llama/llama-cloud-py/commit/48ecb15528509b3a34607ef0cb968d2d38956c3b))
* **api:** api update ([5d70486](https://github.com/run-llama/llama-cloud-py/commit/5d70486e29d0ad50cb41a5a350d7b68ea3b862e2))
* **api:** better deprecation config ([22e56e5](https://github.com/run-llama/llama-cloud-py/commit/22e56e58f63c1420f1f40392ed69328567984031))

## 1.5.0 (2026-03-03)

Full Changelog: [v1.4.1...v1.5.0](https://github.com/run-llama/llama-cloud-py/compare/v1.4.1...v1.5.0)

### Features

* **api:** api update ([0537b16](https://github.com/run-llama/llama-cloud-py/commit/0537b16dd8f8588160d6c1469f0f9821dff6435e))
* **api:** api update ([0deee0e](https://github.com/run-llama/llama-cloud-py/commit/0deee0e231533b60f75e2fb44434bb3c8b287d93))
* **api:** api update ([dededce](https://github.com/run-llama/llama-cloud-py/commit/dededce0585c70ec82b3b1ce2b4ea7b11559de60))
* **api:** api update ([855c7e3](https://github.com/run-llama/llama-cloud-py/commit/855c7e3d51cbb6e08f4cebcbbcd1f77088fea0f3))


### Chores

* **internal:** add request options to SSE classes ([6094c9f](https://github.com/run-llama/llama-cloud-py/commit/6094c9f8c678e748f26a7b35954d24871e08a58b))
* **internal:** make `test_proxy_environment_variables` more resilient ([a025797](https://github.com/run-llama/llama-cloud-py/commit/a025797e811f3c47a657abf29fd806c0bfd61dca))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([7edce65](https://github.com/run-llama/llama-cloud-py/commit/7edce65945fe2721d288e630aa94cc708837ea0b))
* **internal:** remove mock server code ([35ae99c](https://github.com/run-llama/llama-cloud-py/commit/35ae99cc5a7ac3abb6c49da4e2c7ec6f0ff4807b))
* update mock server docs ([c3031de](https://github.com/run-llama/llama-cloud-py/commit/c3031de3d6a7d93e74a60325480aaa54a1faac99))

## 1.4.1 (2026-02-18)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/run-llama/llama-cloud-py/compare/v1.4.0...v1.4.1)

### Chores

* format all `api.md` files ([32fcd56](https://github.com/run-llama/llama-cloud-py/commit/32fcd56e165cc69515a851fc50b99b429593751e))
* **internal:** fix lint error on Python 3.14 ([5db45de](https://github.com/run-llama/llama-cloud-py/commit/5db45decf8c416919e3a27f4c146ad791e43f9bb))

## 1.4.0 (2026-02-12)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/run-llama/llama-cloud-py/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([ba237e3](https://github.com/run-llama/llama-cloud-py/commit/ba237e3f1c2510c6af462f06f84c3184091a9c8b))


### Bug Fixes

* **types:** correctly define false enum ([9c9182f](https://github.com/run-llama/llama-cloud-py/commit/9c9182fa746a5811bc4d4e83e2a0ed633e83c597))


### Chores

* **api:** minor updates ([e1749b8](https://github.com/run-llama/llama-cloud-py/commit/e1749b83a0d0a60ec8acff9b0bd5d4ebdf8aa26f))
* **internal:** bump dependencies ([460e8d8](https://github.com/run-llama/llama-cloud-py/commit/460e8d84ef5386f55f1261efc82d188578620812))

## 1.3.0 (2026-02-04)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/run-llama/llama-cloud-py/compare/v1.2.0...v1.3.0)

### Features

* **api:** api update ([39e243f](https://github.com/run-llama/llama-cloud-py/commit/39e243f710d7bdf60e8ab877ab12fcb69385f292))
* **api:** manual updates ([5a1a439](https://github.com/run-llama/llama-cloud-py/commit/5a1a4395a12fc5636503c5cd545feac413572661))


### Bug Fixes

* throw error on empty expand parameter in e2e parse method ([02fbe93](https://github.com/run-llama/llama-cloud-py/commit/02fbe933b1182ab24811b96d4047033afbd377af))

## 1.2.0 (2026-01-30)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/run-llama/llama-cloud-py/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([5ae5d42](https://github.com/run-llama/llama-cloud-py/commit/5ae5d4233af1d4a32ffb517ccb53698ca12071b7))
* **api:** api update ([4950cda](https://github.com/run-llama/llama-cloud-py/commit/4950cdab74a4e3bb888027bc2ed31f637e16c207))
* **api:** api update ([69eaf93](https://github.com/run-llama/llama-cloud-py/commit/69eaf939dcd2d4bb6d3966eccd46f14e03e3d146))
* **api:** api update ([21505e6](https://github.com/run-llama/llama-cloud-py/commit/21505e669af80fec2e50e4fd4d52b716c094f35e))
* **api:** manual updates - Google Drive ([eb76f4b](https://github.com/run-llama/llama-cloud-py/commit/eb76f4bd8edf5bfa5ab9ad85a148877493fb8eeb))
* **api:** Reordering resources ([7f8e9aa](https://github.com/run-llama/llama-cloud-py/commit/7f8e9aa951112460f50d1064e51930cb86eaf654))
* **client:** add custom JSON encoder for extended type support ([90b5864](https://github.com/run-llama/llama-cloud-py/commit/90b58643d5ec8701b0492479cb4a65d0258ed674))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([c2d87ea](https://github.com/run-llama/llama-cloud-py/commit/c2d87ea743e52c8fa8a1fe631d13432f84f40023))

## 1.1.0 (2026-01-24)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/run-llama/llama-cloud-py/compare/v1.0.0...v1.1.0)

### Features

* **api:** api update ([4c5af6d](https://github.com/run-llama/llama-cloud-py/commit/4c5af6d04a27a63c0674f563809a72d5bf6675dd))
* **api:** api update ([8cbc29f](https://github.com/run-llama/llama-cloud-py/commit/8cbc29f4547e01ab7b4b2a9a190a0edd57eead4f))


### Chores

* **ci:** upgrade `actions/github-script` ([0be2b3c](https://github.com/run-llama/llama-cloud-py/commit/0be2b3c6427029cba2c9d000d5ee38ef9ba2395a))

## 1.0.0 (2026-01-21)

Full Changelog: [v1.0.0-beta.7...v1.0.0](https://github.com/run-llama/llama-cloud-py/compare/v1.0.0-beta.7...v1.0.0)

### Features

* **api:** api update ([fcfeefb](https://github.com/run-llama/llama-cloud-py/commit/fcfeefbbe1905a3cb6f5514de065998d167b7968))

## 1.0.0-beta.7 (2026-01-20)

Full Changelog: [v1.0.0-beta.6...v1.0.0-beta.7](https://github.com/run-llama/llama-cloud-py/compare/v1.0.0-beta.6...v1.0.0-beta.7)

## 1.0.0-beta.6 (2026-01-19)

Full Changelog: [v1.0.0-beta.5...v1.0.0-beta.6](https://github.com/run-llama/llama-cloud-py/compare/v1.0.0-beta.5...v1.0.0-beta.6)

### Features

* **api:** api update ([a2bbe4d](https://github.com/run-llama/llama-cloud-py/commit/a2bbe4de7b2827f99fb211059bebe7d3900f176d))


### Chores

* **internal:** update `actions/checkout` version ([77fe7c0](https://github.com/run-llama/llama-cloud-py/commit/77fe7c0d78fa243bba2b4aef380b4b6e62bd7212))

## 1.0.0-beta.5 (2026-01-17)

Full Changelog: [v1.0.0-beta.4...v1.0.0-beta.5](https://github.com/run-llama/llama-cloud-py/compare/v1.0.0-beta.4...v1.0.0-beta.5)

### Features

* **api:** api update ([60cad6a](https://github.com/run-llama/llama-cloud-py/commit/60cad6afcfbe4723baea80c0590826d9272676d0))


### Bug Fixes

* Parse example in comment ([d5c8ed7](https://github.com/run-llama/llama-cloud-py/commit/d5c8ed79d8ee05019ccff98fe52c5183670e2d67))

## 1.0.0-beta.4 (2026-01-16)

Full Changelog: [v1.0.0-beta.3...v1.0.0-beta.4](https://github.com/run-llama/llama-cloud-py/compare/v1.0.0-beta.3...v1.0.0-beta.4)

### Features

* **api:** api update ([4a23421](https://github.com/run-llama/llama-cloud-py/commit/4a23421a36a23a765afffa3526ace922191c1300))
* **api:** Consolidate more pagination, rename functions ([0b099f3](https://github.com/run-llama/llama-cloud-py/commit/0b099f3f9b691b9045935e8dc0bd51b88f25eaf6))
* **api:** update via SDK Studio ([318a8e9](https://github.com/run-llama/llama-cloud-py/commit/318a8e976b89e3f44b23ef8396d6faaf5bc243e3))
* **api:** update via SDK Studio ([5dd21ce](https://github.com/run-llama/llama-cloud-py/commit/5dd21ce6aedf524101c2052f072f3593f11cd9a7))
* **api:** update via SDK Studio ([18385da](https://github.com/run-llama/llama-cloud-py/commit/18385daf200044012e2ae466807f9a33f660a498))
* **api:** update via SDK Studio ([48879bc](https://github.com/run-llama/llama-cloud-py/commit/48879bc4ece770f5e8506ee00eee3f2093a4932b))
* **api:** update via SDK Studio ([bd46c8b](https://github.com/run-llama/llama-cloud-py/commit/bd46c8b14a66e950bf291e96ca8b4a06dd1c731d))

## 1.0.0-beta.3 (2026-01-14)

Full Changelog: [v0.20.0...v1.0.0-beta.3](https://github.com/run-llama/llama-cloud-py/compare/v0.20.0...v1.0.0-beta.3)

### Features

* **api:** manual updates ([c23da58](https://github.com/run-llama/llama-cloud-py/commit/c23da58fc7096b490c1083d98654cd9bc3db36c1))
* **client:** add support for binary request streaming ([d6cbf95](https://github.com/run-llama/llama-cloud-py/commit/d6cbf954f2c8b7a29a44b8929acc7c76501720fe))


### Chores

* **internal:** codegen related update ([95d0c9a](https://github.com/run-llama/llama-cloud-py/commit/95d0c9abbc779d791fa72acc6ecc53808cacbec3))
* update SDK settings ([0a091c1](https://github.com/run-llama/llama-cloud-py/commit/0a091c12d0b88332786a1e2ba538b027ba41e6aa))

## 0.20.0 (2026-01-14)

Full Changelog: [v0.19.1...v0.20.0](https://github.com/run-llama/llama-cloud-py/compare/v0.19.1...v0.20.0)

### Features

* **api:** api update ([725a04e](https://github.com/run-llama/llama-cloud-py/commit/725a04ec0adc9360b572027a8eaf95e9246e9639))
* **api:** parse v2alpha1 -&gt; v2 ([83fa7c4](https://github.com/run-llama/llama-cloud-py/commit/83fa7c47a1681a4284ca06d8e61a67540c15d4c6))
* **api:** Removing false upload_file endpoint ([d05898c](https://github.com/run-llama/llama-cloud-py/commit/d05898c21995f17a5bebffa9d53e3140b6bb0d2b))
* **api:** Removing false upload_file endpoint ([ff905f1](https://github.com/run-llama/llama-cloud-py/commit/ff905f17f3d7bf0f3db2639db54652f3598a10f8))


### Chores

* configure new SDK language ([5249848](https://github.com/run-llama/llama-cloud-py/commit/5249848c58c9420bfebc9157969627d368e77bb7))

## 0.19.1 (2026-01-10)

Full Changelog: [v0.19.0...v0.19.1](https://github.com/run-llama/llama-cloud-py/compare/v0.19.0...v0.19.1)

## 0.19.0 (2026-01-10)

Full Changelog: [v0.18.0...v0.19.0](https://github.com/run-llama/llama-cloud-py/compare/v0.18.0...v0.19.0)

### Features

* **api:** api update ([028190e](https://github.com/run-llama/llama-cloud-py/commit/028190ed0b7c0f5e4eee8f913cb13f3745ad3ecc))
* **api:** manual updates ([3616730](https://github.com/run-llama/llama-cloud-py/commit/36167303b3980a45b56039d959435a35c6d866c8))

## 0.18.0 (2026-01-08)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/run-llama/llama-cloud-py/compare/v0.17.0...v0.18.0)

### Features

* **api:** add list commands to pipeline file images ([e9ac62e](https://github.com/run-llama/llama-cloud-py/commit/e9ac62ecfee8b9020e169010cc910989dc491c78))

## 0.17.0 (2026-01-06)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/run-llama/llama-cloud-py/compare/v0.16.0...v0.17.0)

### Features

* **api:** api update ([b4a17d8](https://github.com/run-llama/llama-cloud-py/commit/b4a17d84ae557c68ea5186481b1e2bf0bade435a))

## 0.16.0 (2026-01-06)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/run-llama/llama-cloud-py/compare/v0.15.0...v0.16.0)

### Features

* **api:** add back pipeline files ([ca81b27](https://github.com/run-llama/llama-cloud-py/commit/ca81b27d04ee0bdeb0484d6638509197a6f9cb1b))
* **api:** add pipelines image utils ([dd26528](https://github.com/run-llama/llama-cloud-py/commit/dd26528422b7053e132470f4498fac26d4f6e168))
* **api:** api update ([31d2071](https://github.com/run-llama/llama-cloud-py/commit/31d2071597fe67d2b397bc441e354451de60bc95))
* **api:** api update ([064c1ad](https://github.com/run-llama/llama-cloud-py/commit/064c1adeb43804de1e1acdc00b4fcd187f7ee2ce))
* **api:** Fix readme ([54cb781](https://github.com/run-llama/llama-cloud-py/commit/54cb7817269c3751562f05e550b5691eb8a74276))
* **api:** swap in files v2 support ([fbd41a4](https://github.com/run-llama/llama-cloud-py/commit/fbd41a4abae1f02b39f61d576befcad9c903b2b6))
* **api:** typo ([3e8bce8](https://github.com/run-llama/llama-cloud-py/commit/3e8bce86f76f09bd708cc246247ad60b1976fb56))

## 0.15.0 (2026-01-06)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/run-llama/llama-cloud-py/compare/v0.14.0...v0.15.0)

### Features

* **api:** api update ([1c43170](https://github.com/run-llama/llama-cloud-py/commit/1c43170b98fbad88a24295db44527cf06f4d2c2a))
* **api:** api update ([dec9b8b](https://github.com/run-llama/llama-cloud-py/commit/dec9b8b1b34f990821f7d967878dc362bfc5c19e))


### Chores

* **internal:** codegen related update ([fb629e4](https://github.com/run-llama/llama-cloud-py/commit/fb629e4cf0dacd3a708cc4705ccc9e0c3fd542be))

## 0.14.0 (2025-12-23)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/run-llama/llama-cloud-py/compare/v0.13.0...v0.14.0)

### Features

* **api:** api update ([f51c7dc](https://github.com/run-llama/llama-cloud-py/commit/f51c7dcd316db757103b8429a372bde2d4aaa0ea))
* **api:** api update ([ff5295d](https://github.com/run-llama/llama-cloud-py/commit/ff5295ddccab0cf23ce854c9e393ced2f114f8db))
* **api:** api update ([5335d08](https://github.com/run-llama/llama-cloud-py/commit/5335d085a7cded66214f8d74ba1ff9f2fadc490f))
* **api:** api update ([68dabd1](https://github.com/run-llama/llama-cloud-py/commit/68dabd199971a8cd1fa43d781725ef733be466d5))
* **api:** api update ([20cbc0d](https://github.com/run-llama/llama-cloud-py/commit/20cbc0d9d57a06cc448e7cc6f7d9cf9e72a5ec38))
* **api:** api update ([5be72ef](https://github.com/run-llama/llama-cloud-py/commit/5be72ef51bb7be7ad44ac1085ca24885bf7dbc81))
* **api:** parse v2 updates ([6d8e09c](https://github.com/run-llama/llama-cloud-py/commit/6d8e09cb5e729bcf6095ba3a99f7591059fbd0e3))
* **api:** swap in parse v2 support ([0134a13](https://github.com/run-llama/llama-cloud-py/commit/0134a13d5c013fcce6943105098587bb60828439))
* **api:** update readme ([4d21124](https://github.com/run-llama/llama-cloud-py/commit/4d21124abf414ffbbca5ed36dc39074d4109ed8a))
* **api:** use repeat query params with and char ([054c5ac](https://github.com/run-llama/llama-cloud-py/commit/054c5ac34d65b0aa64082ac7d3983a63ff789d65))


### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([a8a44f6](https://github.com/run-llama/llama-cloud-py/commit/a8a44f6b6a3cf622d807100517b325b94875f9ed))
* use async_to_httpx_files in patch method ([f137ed7](https://github.com/run-llama/llama-cloud-py/commit/f137ed7ca66be65fb5917ac0739a6243b549e255))


### Chores

* add missing docstrings ([f5b5cf9](https://github.com/run-llama/llama-cloud-py/commit/f5b5cf90f95785bc59332ffec6a1d8bd4040b24d))
* **internal:** add `--fix` argument to lint script ([4a5d9d0](https://github.com/run-llama/llama-cloud-py/commit/4a5d9d0f73c423828c3cc6a46cc0b09067776e43))
* **internal:** add missing files argument to base client ([cfd8fc8](https://github.com/run-llama/llama-cloud-py/commit/cfd8fc8da24d63ed6669c17bda54e2e081bdfa17))
* speedup initial import ([98e32fc](https://github.com/run-llama/llama-cloud-py/commit/98e32fcb35dbc9762ba8b57658aefb06535a2ffc))

## 0.13.0 (2025-12-04)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/run-llama/llama-cloud-py/compare/v0.12.0...v0.13.0)

### Features

* **api:** add list page screenshots/figures ([e4c618c](https://github.com/run-llama/llama-cloud-py/commit/e4c618c4046da38d0d4234f934c6a80f782839ce))

## 0.12.0 (2025-12-03)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/run-llama/llama-cloud-py/compare/v0.11.0...v0.12.0)

### Features

* **api:** add split ([2219e71](https://github.com/run-llama/llama-cloud-py/commit/2219e712b4ab3a196b04e425a73b7e2af52bed43))


### Chores

* **docs:** use environment variables for authentication in code snippets ([f054d44](https://github.com/run-llama/llama-cloud-py/commit/f054d44d903f850e2503029f2399f4cee10606ae))
* update lockfile ([3f8db4e](https://github.com/run-llama/llama-cloud-py/commit/3f8db4ea90ea3c268c3f59dd9cb2da7166e61f50))

## 0.11.0 (2025-12-03)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/run-llama/llama-cloud-py/compare/v0.10.0...v0.11.0)

### Features

* **api:** add some missing endpoints ([f5dbc21](https://github.com/run-llama/llama-cloud-py/commit/f5dbc213944ce8745026ca7beb65c407551b8a75))
* **api:** api update ([609d9be](https://github.com/run-llama/llama-cloud-py/commit/609d9be78a50a9dc982b251ab5a78540d2c183a6))
* **api:** api update ([293983f](https://github.com/run-llama/llama-cloud-py/commit/293983f07682026038d2a36c4e8cf51d284cc597))

## 0.10.0 (2025-12-01)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/run-llama/llama-cloud-py/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([981b2ea](https://github.com/run-llama/llama-cloud-py/commit/981b2ea0a185083d61519b1231f0a7d482e48054))
* **api:** fix readme example ([b615fbf](https://github.com/run-llama/llama-cloud-py/commit/b615fbf2b32e4dbf9e3eb162f25c145451cadc7a))

## 0.9.0 (2025-12-01)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/run-llama/llama-cloud-py/compare/v0.8.0...v0.9.0)

### Features

* **api:** add pipeline.retrieve method ([cd02c34](https://github.com/run-llama/llama-cloud-py/commit/cd02c34bd8fc89c08a1baf05432fccef2bb2aee7))
* **api:** api update ([c86b1a4](https://github.com/run-llama/llama-cloud-py/commit/c86b1a48c483384179e8fa9aff1adecac8c11149))

## 0.8.0 (2025-11-28)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/run-llama/llama-cloud-py/compare/v0.7.0...v0.8.0)

### Features

* **api:** add get page figure/screenshot methods ([388d86e](https://github.com/run-llama/llama-cloud-py/commit/388d86e0d6a749632ef2deb00ee1917b00df9aba))

## 0.7.0 (2025-11-28)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/run-llama/llama-cloud-py/compare/v0.6.0...v0.7.0)

### Features

* **api:** add back projects list/get ([b6b41a1](https://github.com/run-llama/llama-cloud-py/commit/b6b41a1d0289452e64c3440d9c414854155d82dd))
* **api:** api update ([fdd82e0](https://github.com/run-llama/llama-cloud-py/commit/fdd82e082bdfc3b237a815dc9255b469fdb19dfe))


### Bug Fixes

* ensure streams are always closed ([7f1be5b](https://github.com/run-llama/llama-cloud-py/commit/7f1be5b2c486da8f17dd2315eceb9d1ea465172f))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([9a79655](https://github.com/run-llama/llama-cloud-py/commit/9a796552cca42dcfc3b58a15afe350fed4eb7c83))

## 0.6.0 (2025-11-27)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/run-llama/llama-cloud-py/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([652a7a8](https://github.com/run-llama/llama-cloud-py/commit/652a7a8ad5ada51a312c965d04e7726895f44f8c))

## 0.5.0 (2025-11-27)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/run-llama/llama-cloud-py/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([0c5e51f](https://github.com/run-llama/llama-cloud-py/commit/0c5e51fe3ea77ac4b2f4776dee77be261806eed8))
* **api:** manual updates ([2d593a1](https://github.com/run-llama/llama-cloud-py/commit/2d593a16432cbf54bad7ea74d80c095888204d7a))

## 0.4.0 (2025-11-26)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/run-llama/llama-cloud-py/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([1c11d9d](https://github.com/run-llama/llama-cloud-py/commit/1c11d9d8763217a43e660950b8646b4e649a96be))
* **api:** fix api key name ([85e9cb3](https://github.com/run-llama/llama-cloud-py/commit/85e9cb3c94000b7c639bdb5fcfe7b263bf1acc83))
* **api:** manual updates ([a03d412](https://github.com/run-llama/llama-cloud-py/commit/a03d41232fe84af09fdfcdb30d0ac5f16962595a))
* **api:** update extract API endpoints ([7c30619](https://github.com/run-llama/llama-cloud-py/commit/7c306198d06dd508c4f2a0499692cd74c6266ae4))

## 0.3.0 (2025-11-23)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/run-llama/llama-cloud-py/compare/v0.2.0...v0.3.0)

### Features

* **api:** Add missing api endpoints ([c8e9c07](https://github.com/run-llama/llama-cloud-py/commit/c8e9c0775a1fa6409e6fab5429d9fbaffed0526b))
* **api:** api update ([c4dac52](https://github.com/run-llama/llama-cloud-py/commit/c4dac5205f77ce7cf256a27b3c86d8a2b49828e7))
* **api:** api update ([e1ff8b1](https://github.com/run-llama/llama-cloud-py/commit/e1ff8b12c0759cd0750f68c84bd5a6a3730e95f1))
* **api:** api update ([01f2af5](https://github.com/run-llama/llama-cloud-py/commit/01f2af5dbe77c6203c80368f239b0e9e14d041a6))
* **api:** manual updates ([e6efd22](https://github.com/run-llama/llama-cloud-py/commit/e6efd22383c2c3a4b26e50534be25683fdfcf246))
* **api:** manual updates ([2a52d8c](https://github.com/run-llama/llama-cloud-py/commit/2a52d8c87e940d558198cf434f0400e97a8af144))
* **api:** manual updates ([088fbcc](https://github.com/run-llama/llama-cloud-py/commit/088fbccd80a975ea05ca3d5ff44a77497fdb52f2))
* **api:** manual updates ([70248a5](https://github.com/run-llama/llama-cloud-py/commit/70248a5c9198c455c3a704cb24790da8524af07b))
* **api:** manual updates ([ffc9c2c](https://github.com/run-llama/llama-cloud-py/commit/ffc9c2cfa2dde27f05507fd1922c2ea1787f3d6c))
* **api:** manual updates ([571deab](https://github.com/run-llama/llama-cloud-py/commit/571deab5d900476ac4c1dbb0bf71f11ec381ba1f))
* **api:** manual updates ([8f19b18](https://github.com/run-llama/llama-cloud-py/commit/8f19b18152ddb24bbbc7e467d6ca1e6e78335853))
* **api:** manual updates ([8794d62](https://github.com/run-llama/llama-cloud-py/commit/8794d62ca0dc827f2f5cd00f42fe6272c34cd442))
* **api:** manual updates ([6f90a08](https://github.com/run-llama/llama-cloud-py/commit/6f90a0856da964070c061225c189b14bb635634f))
* **api:** manual updates ([2f47fa9](https://github.com/run-llama/llama-cloud-py/commit/2f47fa9713ea35bcb02bc80d9e36415a97cf7a58))
* **api:** manual updates ([82bcafa](https://github.com/run-llama/llama-cloud-py/commit/82bcafa88fbcedfaea163e5b95d3da50b878c011))
* **api:** manual updates ([abed126](https://github.com/run-llama/llama-cloud-py/commit/abed1261c6dbc0cb1a8fc07191516c34e947ea72))
* **api:** manual updates ([d4c400b](https://github.com/run-llama/llama-cloud-py/commit/d4c400bfd30e982b6cbccee7f5dbac6215bd5da9))
* **api:** remove some agent items ([8282fa2](https://github.com/run-llama/llama-cloud-py/commit/8282fa2a7d37ae04d8d68091eb99ab124ff1e425))


### Chores

* add Python 3.14 classifier and testing ([5c8f944](https://github.com/run-llama/llama-cloud-py/commit/5c8f944ce59e39565f5fcba65fb65d33e9f6d732))

## 0.2.0 (2025-11-19)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/run-llama/llama-cloud-py/compare/v0.1.1...v0.2.0)

### Features

* **api:** api update ([02e9e08](https://github.com/run-llama/llama-cloud-py/commit/02e9e088adfe7842c3a098e816aa6930ae156e86))


### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([9784558](https://github.com/run-llama/llama-cloud-py/commit/97845584d969cf89fb7b28f4d5acea26055c0e50))

## 0.1.1 (2025-11-11)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/run-llama/llama-cloud-py/compare/v0.1.0...v0.1.1)

### Bug Fixes

* compat with Python 3.14 ([198061d](https://github.com/run-llama/llama-cloud-py/commit/198061d9a14a632331aee4300e2c4fe3a39e10d8))


### Chores

* **package:** drop Python 3.8 support ([dba8e3a](https://github.com/run-llama/llama-cloud-py/commit/dba8e3a953a3f5d29a5357fd7c46babfd2e9b7cb))

## 0.1.0 (2025-11-07)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/run-llama/llama-cloud-py/compare/v0.0.1...v0.1.0)

### Features

* **api:** add pagination config ([a09a6bf](https://github.com/run-llama/llama-cloud-py/commit/a09a6bf431ddd321b14a6c5574117690f7cbae00))
* **api:** api update ([5e2aade](https://github.com/run-llama/llama-cloud-py/commit/5e2aade9aefa461b215f37fe60239cea20c98cf8))
* **api:** api update ([64c9670](https://github.com/run-llama/llama-cloud-py/commit/64c9670fcf95169273929d13fc46c2b11efd62b5))
* **api:** api update ([34f9ead](https://github.com/run-llama/llama-cloud-py/commit/34f9ead6480e2bb8176e73b92e21bcac2c4998df))
* **api:** api update ([3b2842f](https://github.com/run-llama/llama-cloud-py/commit/3b2842f681a011d56ccf7b7eb9d0b0fa5938bbae))
* **api:** api update ([4e3731c](https://github.com/run-llama/llama-cloud-py/commit/4e3731c85afd4efaa2492b36ff72ced402a1df2b))
* **api:** api update ([aad8635](https://github.com/run-llama/llama-cloud-py/commit/aad8635110d562f64e08e84d2dc3552066b174be))
* **api:** clean up schemas ([0e93369](https://github.com/run-llama/llama-cloud-py/commit/0e9336946b3ef953ed1e851621a5bba393971ef0))
* **api:** fix pagination example in readme ([7bdd2b6](https://github.com/run-llama/llama-cloud-py/commit/7bdd2b66e7ece7923c0a3341d32ecfe830ad41eb))
* **api:** manual updates ([dd6fde5](https://github.com/run-llama/llama-cloud-py/commit/dd6fde5feb15a8a47f5ef22342dbe1e5b251a3a0))
* **api:** manual updates ([a4fb399](https://github.com/run-llama/llama-cloud-py/commit/a4fb39918251947b112db1159c5cd4fc954d3751))
* **api:** manual updates ([1015a46](https://github.com/run-llama/llama-cloud-py/commit/1015a4645225859fd76d303e72c5e32262bdec3d))
* **api:** manual updates ([9aaa486](https://github.com/run-llama/llama-cloud-py/commit/9aaa486baa8071d1bced680c458a522368352d52))
* **api:** more cleanup ([daee74d](https://github.com/run-llama/llama-cloud-py/commit/daee74d609630bf1b4690c01d15119f99c96ec8e))
* **api:** update readme ([bf4d489](https://github.com/run-llama/llama-cloud-py/commit/bf4d489a8fd70c48923311e1cdf92716c9cfdfb8))


### Bug Fixes

* **client:** close streams without requiring full consumption ([243dea9](https://github.com/run-llama/llama-cloud-py/commit/243dea98df257f78ccf52a3baea18e1021ed4781))


### Chores

* configure new SDK language ([21510df](https://github.com/run-llama/llama-cloud-py/commit/21510df5cbe886f1fcb5e9e9d542bf7369c25ce9))
* **internal/tests:** avoid race condition with implicit client cleanup ([cc38e89](https://github.com/run-llama/llama-cloud-py/commit/cc38e89f51106fee9df9d4b3db1bed3e3c0145d2))
* **internal:** grammar fix (it's -&gt; its) ([f0c3628](https://github.com/run-llama/llama-cloud-py/commit/f0c36285f6ea54ffeb7231bc6cd55b89f4272f3b))
