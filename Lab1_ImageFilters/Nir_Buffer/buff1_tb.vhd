library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Buff1_tb is
end Buff1_tb;

architecture Behavioral of Buff1_tb is
    -- Parameters
    constant COLOR_DEPTH : integer := 8;    -- Number of bits per pixel
    constant ROW_WIDTH   : integer := 3;    -- Number of pixels in a row (simplified for testing)

    -- Signals to connect to the DUT
    signal clk          : std_logic := '0';
    signal rst          : std_logic := '0';
    signal current_row  : std_logic_vector((ROW_WIDTH * COLOR_DEPTH) - 1 downto 0);
    signal low_row      : std_logic_vector((ROW_WIDTH * COLOR_DEPTH) +15 downto 0);
    signal mid_row      : std_logic_vector((ROW_WIDTH * COLOR_DEPTH) +15 downto 0);
    signal hig_row      : std_logic_vector((ROW_WIDTH * COLOR_DEPTH) +15 downto 0);

    -- Clock period
    constant CLK_PERIOD : time := 10 ns;
begin

    -- DUT Instantiation
    DUT: entity work.Buff1
        generic map (
            COLOR_DEPTH => COLOR_DEPTH,
            ROW_WIDTH   => ROW_WIDTH
        )
        port map (
            clk         => clk,
            rst         => rst,
            current_row => current_row,
            low_row     => low_row,
            mid_row     => mid_row,
            hig_row     => hig_row
        );

    -- Clock Generation
    clk_process: process
    begin
        clk <= '0';
        wait for CLK_PERIOD / 2;
        clk <= '1';
        wait for CLK_PERIOD / 2;
    end process;

    -- Stimulus Process
    stimulus_process: process
    begin
        -- Reset the DUT
        rst <= '1';  -- Assert reset
        wait for 2 * CLK_PERIOD;  -- Hold reset for 2 clock cycles
        rst <= '0';  -- Deassert reset

        -- Apply input rows
        current_row <= "000000010000001100000010";  -- Row: 132
        wait for CLK_PERIOD;

        current_row <= "000000010000001000000001";  -- Row: 121
        wait for CLK_PERIOD;

        current_row <= "000000110000000100000001";  -- Row: 311
        wait for CLK_PERIOD;

      

        -- End Simulation
        wait;
    end process;

end Behavioral;

