#!/bin/bash
cd "$(dirname "$0")/../.."
rm -f out/verif_adenda07/run_fx.done out/verif_adenda07/run_refx.done
bash out/verif_adenda07/run_fx.sh
bash out/verif_adenda07/run_refx.sh
