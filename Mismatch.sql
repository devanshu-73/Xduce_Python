-- Create or replace the temp view 'claimmismatch' 
CREATE OR REPLACE TEMP VIEW claimmismatch AS
SELECT 
    COALESCE(plt.claimnumber, ft.claimnumber) AS claimnumber_plt,
    plt.Segment AS reportgroup_plt,
    plt.Total_loss AS Total_loss_plt,
    COALESCE(ft.claimnumber, plt.claimnumber) AS claimnumber_ft,
    ft.SegmentCode AS reportgroup_ft,
    ft.Total_loss AS Total_loss_ft,
    NVL(plt.Total_loss, 0) - NVL(ft.Total_loss, 0) AS Diff,
    CASE 
        WHEN plt.claimnumber IS NULL AND ft.claimnumber IS NOT NULL THEN 'Claim only in Ft'
        WHEN ft.claimnumber IS NULL AND plt.claimnumber IS NOT NULL THEN 'Claim only in Platinum'
        WHEN NVL(plt.Total_loss, 0) <> NVL(ft.Total_loss, 0) THEN 'Loss Mismatch'
        WHEN plt.Segment <> ft.SegmentCode THEN 'Segment Mismatch'
        ELSE 'Match'
    END AS Category
FROM (
    SELECT 
        claimnumber, 
        Segment,
        ROUND(SUM(NVL(loss, 0)), 2) AS Total_loss
    FROM lossess
    WHERE LEFT(AcctgPeriod, 4) <= '2023'
        AND claimnumber IS NOT NULL
    GROUP BY claimnumber, Segment
) plt
FULL OUTER JOIN (
    SELECT 
        ClaimNumber,
        SegmentCode,
        ROUND(SUM(NVL(PaidLoss, 0) + NVL(PaidALAE, 0) + NVL(Recovery, 0) + NVL(LossReserve, 0) + NVL(ALAEReserve, 0)), 2) AS Total_loss
    FROM dsi_reg.adv_db_recon.ft_loss_detail
    WHERE LEFT(AccountingPeriod, 4) <= '2023'
        AND ClaimSourceCode = '105'
    GROUP BY ClaimNumber, SegmentCode
) ft
ON (ft.ClaimNumber = plt.claimnumber AND ft.SegmentCode = plt.Segment);

-- Query the 'claimmismatch' view
SELECT * FROM claimmismatch
WHERE 
    NOT (claimnumber_plt IS NULL OR claimnumber_plt <=> '.')
    AND (Category = 'Loss Mismatch' OR Category = 'Segment Mismatch')
ORDER BY claimnumber_plt, claimnumber_ft;
