# Decision Log

## D-001 Preserve exact requested plant inventory
Status: ACCEPTED
Reason: user explicitly wants this exact garden rather than a generic optimized replacement.

## D-002 Do not lock physical coordinates before site geometry
Status: ACCEPTED
Reason: exact layout without dimensions/sun map would create false precision.

## D-003 Separate permanent crops
Status: ACCEPTED
Applies to: asparagus, rhubarb, roses, durable perennial ornamentals.
Reason: avoid disrupting annual rotation and reconfiguration.

## D-004 Split herbs by water/drainage need
Status: ACCEPTED
Reason: “herbs” are not a valid irrigation hydrozone.

## D-005 Keep software optional and portable
Status: ACCEPTED
Canonical truth starts in human-readable files + structured CSV/JSON. Automation layers must be detachable.

## D-006 Red rose theme remains dominant
Status: ACCEPTED
One optional white backyard rose is allowed; no other rose color creep without explicit user change.
