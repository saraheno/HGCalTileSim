# HGCal Tile

GEANT4-based simulation of CE-H HGCal scintillator tile.

## Installing

The program can be can be installed in two methods. One is a standalone package
meant to be used for event display and debugging. The other is to be compiled
under CMSSW for for batch running and plotting.

For standalone installation (on hepcms.umd.edu or any Linux machine). The
`source` command is only needed if you do not already have Geant4/ROOT installed
on your system.

```bash
git clone https://github.com/yimuchen/HGCal-Dimple-Tile.git HGCalTileSim
cd     HGCalTileSim
source ./g4env.sh # If you do not have Geant4 already installed
cmake .
cmake --build .
```

For the CMSSW installation, run the commented command if you want to use the
inbuilt plotting scripts.

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc700
cmsrel CMSSW_10_3_1_patch1
cd CMSSW_10_3_1_patch1/src
cmsenv

git clone https://github.com/yimuchen/HGCal-Dimple-Tile.git HGCalTileSim
git clone https://github.com/yimuchen/UserUtils.git UserUtils
scram b
```

## Single event running

For the interactive running, run the command following commands

```bash
./bin/LYSim
#$CMSSW_BASE/bin/${SCRAM_ARCH}/LYSim_Session  # In CMSSW
```

You should be greeted with the Geant4 prompt and a detector viewing window. You
can alter detector parameters from using the many `/LYSim` commands

```bash
/LYSim/SetDimpleIndent 1.5 mm
/LYSim/SetPhotonMult 0.01
```

and run a number of event via the command:

```bash
/run/beamOn 10 # 10 Events
```

You can then browse the events in the viewing window. After you have closed the
program, you can also see the saved results in the `Interactive_Session.root`
file.

For debugging, run the command:

```bash
./bin/LYSim DEBUG
#$CMSSW_BASE/bin/${SCRAM_ARCH}/LYSim_Session DEBUG  # In CMSSW
```

In this setup, the particle source is a single optical photon source that one can
set the position and direction:

```bash
/LYSim/Debug/SetParticlePosition 0 0 -1 mm
/LYSim/Debug/SetParticleDirection 0 5 10
```

## Bulk running

In the CMSSW, one has can run the program
`$CMSSW_BASE/bin/${SCRAM_ARCH}/LYSim_SquareTrigger` with multiple options:

```bash
>> $CMSSW_BASE/bin/slc6_amd64_gcc700/LYSim_SquareTrigger --help
  -h [ --help ]                     print help options and exit program

Running a run with a certain geometry:
  -x [ --beamx ] arg (=0)           x center of beam [mm]
  -y [ --beamy ] arg (=0)           y center of beam [mm]
  -w [ --beamwidth ] arg (=0)       width of beam [mm]
  -r [ --dimplerad ] arg (=3)       Dimple radius [mm]
  -d [ --dimpleind ] arg (=1.5)     Dimple indent [mm]
  -a [ --absmult ] arg (=1)         Multple of inbuilt absorption length
  -m [ --wrapreflect ] arg (=1)     Wrap reflectivity
  -N [ --NEvents ] arg (=1)         Number of events to run
  -o [ --output ] arg (=test.root)  output file
```

This will generate a root file of a single configuration with many number of
events (it takes about 2-4seconds for each event so estimate your runtime
accordingly). For example:

```bash
$CMSSW_BASE/bin/slc6_amd64_gcc700/LYSim_SquareTrigger --beamx 2.0 --beamwidth 1.5 --NEvents 1000 --output mytest.root
```

will generate the file `mytest.root` with the muon beam hitting the tile at
x=2.0mm, y=0.0mm, with a uniform square distribution with half-width of 1.5mm,
and will run a total of 1000 events (~1 hour runtime). The user is free to write
your own scripts for generating the required scripts for running under condor.
