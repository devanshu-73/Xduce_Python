CREATE OR REPLACE TEMP VIEW claimmismatch AS
SELECT DISTINCT 
    coalesce(plt.claimnumber, ft.claimnumber) AS claimnumber_plt,
    plt.Cell AS reportgroup_plt,
    plt.Total_loss AS Total_loss_plt,
    coalesce(ft.claimnumber, plt.claimnumber) AS claimnumber_ft,
    ft.CellCode AS reportgroup_ft,
    ft.Total_loss AS Total_loss_ft
FROM (
    SELECT 
        claimnumber,
        Cell,
        ROUND(SUM(NVL(loss, 0)), 2) AS Total_loss
    FROM lossess
    WHERE LEFT(AcctgPeriod, 4) <= 2023
    GROUP BY claimnumber, Cell
) plt
FULL OUTER JOIN (
    SELECT 
        ClaimNumber,
        CellCode,
        ROUND(SUM(NVL(PaidLoss, 0) + NVL(PaidALAE, 0) + NVL(Recovery, 0) + NVL(LossReserve, 0) + NVL(ALAEReserve, 0)), 2) AS Total_loss
    FROM dsi_reg.adv_db_recon.ft_loss_detail
    WHERE LEFT(AccountingPeriod, 4) <= '2023'
      AND ClaimSourceCode = '105'
    GROUP BY ClaimNumber, CellCode
) ft
ON (ft.ClaimNumber = plt.claimnumber AND ft.CellCode = plt.Cell)
WHERE NOT (ft.Total_loss <=> plt.Total_loss)
  AND NOT (plt.Total_loss <=> 0 AND ft.Total_loss IS NULL)
  AND NOT (plt.Total_loss IS NULL AND ft.Total_loss <=> 0);











SELECT * FROM (
    SELECT 
        COALESCE(plt.claimnumber, ft.claimnumber) AS claimnumber_plt,
        plt.Cell AS reportgroup_plt,
        plt.Total_loss AS Total_loss_plt,
        COALESCE(ft.claimnumber, plt.claimnumber) AS claimnumber_ft,
        ft.CellCode AS reportgroup_ft,
        ft.Total_loss AS Total_loss_ft,
        NVL(plt.Total_loss, 0) - NVL(ft.Total_loss, 0) AS Diff,
        CASE 
            WHEN c.claimnumber_plt IS NULL AND plt.claimnumber IS NULL THEN 'Claim only in Ft'
            WHEN c.claimnumber_plt IS NULL AND ft.claimnumber IS NULL THEN 'Claim only in Platinum'
            WHEN c.claimnumber_plt IS NOT NULL THEN 'Loss Mismatch'
            WHEN c.claimnumber_plt IS NULL THEN 'Loss Match'  
        END AS Category
    FROM (
        SELECT 
            claimnumber,
            Cell,
            ROUND(SUM(NVL(loss, 0)), 2) AS Total_loss
        FROM lossess
        WHERE LEFT(AcctgPeriod, 4) <= 2023
          AND claimnumber IS NOT NULL
        GROUP BY claimnumber, Cell
    ) plt
    FULL OUTER JOIN (
        SELECT 
            ClaimNumber,
            CellCode,
            ROUND(SUM(NVL(PaidLoss, 0) + NVL(PaidALAE, 0) + NVL(Recovery, 0) + NVL(LossReserve, 0) + NVL(ALAEReserve, 0)), 2) AS Total_loss
        FROM dsi_reg.adv_db_recon.ft_loss_detail
        WHERE LEFT(AccountingPeriod, 4) <= '2023'
          AND ClaimSourceCode = '105'
        GROUP BY ClaimNumber, CellCode
    ) ft
    ON (ft.ClaimNumber = plt.claimnumber AND ft.CellCode = plt.Cell)
    LEFT JOIN claimmismatch c
    ON (COALESCE(plt.claimnumber, ft.claimnumber) = c.claimnumber_plt)
    WHERE NOT (ft.Total_loss <=> plt.Total_loss)
      AND NOT (plt.Total_loss <=> 0 AND ft.Total_loss IS NULL)
      AND NOT (plt.Total_loss IS NULL AND ft.Total_loss <=> 0)
) 
WHERE NOT (claimnumber_plt IS NULL OR claimnumber_plt <=> '.')
  AND NOT (Category <=> 'Claim only in Ft' OR Category <=> 'Claim only in Platinum')
  AND Category = 'Loss Mismatch'
ORDER BY claimnumber_plt, claimnumber_ft;
